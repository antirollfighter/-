
import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
import json

# 设置为自己的cookies
cookies = {
    'SINAGLOBAL': '1522276477633.3953.1717644808408',
    'SUB': '_2A25Lbt4TDeRhGeNL6lUQ8SbKyD2IHXVoAl_brDV8PUJbkNANLVTXkW1NSTCV64cKwCYuWZnE1ND7DkGtOsVgpb0I',
    'ALF': '1720859459',
    '_s_tentry': 'weibo.com',
    'Apache': '719930130166.0288.1718672999885',
    'ULV': '1718672999889:3:3:2:719930130166.0288.1718672999885:1718103210060',
}


def get_the_list_response(q='话题', n='1', p='页码'):
    headers = {
        'authority': 's.weibo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'referer': 'https://s.weibo.com/weibo?q=%23%E6%80%BB%E4%B9%A6%E8%AE%B0%E5%AF%B9%E8%BF%9B%E4%B8%80%E6%AD%A5%E5%85%A8%E9%9D%A2%E6%B7%B1%E5%8C%96%E6%94%B9%E9%9D%A9%E7%9A%84%E9%87%8D%E8%A6%81%E9%83%A8%E7%BD%B2%23&nodup=1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    }

    params = {
        'q': q,
        'nodup': n,
        'page': p,
    }
    response = requests.get('https://s.weibo.com/weibo', params=params, cookies=cookies, headers=headers)
    return response


def parse_the_list(text):
    soup = BeautifulSoup(text)
    divs = soup.select('div[action-type="feed_list_item"]')
    lst = []
    for div in divs:
        mid = div.get('mid')
        time = div.select('div.card-feed > div.content > div.from > a:first-of-type')
        if time:
            time = time[0].string.strip()
        else:
            time = None
        p = div.select('div.card-feed > div.content > p:last-of-type')
        if p:
            p = p[0].strings
            content = '\n'.join([para.replace('\u200b', '').strip() for para in list(p)]).strip()
        else:
            content = None
        star = div.select('ul > li > a > button > span.woo-like-count')
        if star:
            star = list(star[0].strings)[0]
        else:
            star = None
        lst.append((mid, content, star, time))
    df = pd.DataFrame(lst, columns=['mid', 'content', 'star', 'time'])
    return df


def get_the_list(q, p):
    df_list = []
    for i in range(1, p + 1):
        response = get_the_list_response(q=q, p=i)
        if response.status_code == 200:
            df = parse_the_list(response.text)
            df_list.append(df)
            print(f'第{i}页解析成功！', flush=True)

    return df_list


if __name__ == '__main__':
    # 先设置cookie，换成自己的；
    q = ('老师耗时1年手绘47幅画送毕业生')
    p = 20
    df_list = get_the_list(q, p)
    df = pd.concat(df_list)
    df.to_csv(f'{q}.csv', index=False)
