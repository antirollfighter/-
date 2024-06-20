# -*- coding: utf-8 -*-


from NewSuperWeiboForwardSpider import NewSuperWeiboForward

# cookie 是 filter 搜 repost
forwardSpider = NewSuperWeiboForward(mid='5046977450477909',
                                     cookie='SUB=_2A25Lbt4TDeRhGeNL6lUQ8SbKyD2IHXVoAl_brDV8PUJbkNANLVTXkW1NSTCV64cKwCYuWZnE1ND7DkGtOsVgpb0I; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFwU3I6ycKm5LQh.UVTYLk05JpX5KMhUgL.Fo-feKMpeKnce022dJLoIpYLxKnL1K5LB.BLxKnL1K5LB.BLxKMLBK-L1--Eeh2f; ULV=1718672999889:3:3:2:719930130166.0288.1718672999885:1718103210060; PC_TOKEN=21cb4a60c8; WBStorage=267ec170|undefined; XSRF-TOKEN=f9PO6Gu0j7Q-o5ckXYVZDB9f; WBPSESS=fe5hhK1OwTgd_ZmPdVJVQjlrljk2CqtoX2b-NTKYcD5yXBew4sOvQwwfAyyBd_5wz1AoxSqpLKlBJER7ssfmMXsar8xueBZzaXflxSxHCWe4cptEj4b0tFLZ2_UJuaUdWP8WZNBHFNn-4ePhUt1NzA==')
forwardSpider.crawl()
