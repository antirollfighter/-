# -*- coding: utf-8 -*-


from NewSuperWeiboForwardSpider import NewSuperWeiboForward

weibo_link_list = [
    'https://weibo.com/2500935572/No7VVw365',
    'https://weibo.com/7570263046/NpBLFekC6'
]
for weibo_link in weibo_link_list:
    if '?' in weibo_link:
        weibo_link = weibo_link[:weibo_link.rindex('?')]
    if '#' in weibo_link:
        weibo_link = weibo_link[:weibo_link.rindex('#')]
    mid_or_wid = weibo_link[weibo_link.rindex('/')+1:]
    # cookie 是 filter 搜 repost
    forwardSpider = NewSuperWeiboForward(mid=mid_or_wid,
                                         cookie='')
    forwardSpider.crawl()
