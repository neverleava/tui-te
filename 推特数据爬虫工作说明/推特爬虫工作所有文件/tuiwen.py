import json
import stweet as st
import pandas as pd
import xlwt
import csv
from datetime import datetime

#
#
#
dat = []
dat1=[]
with open('output_raw_search_tweets.jl', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        ap = tweet['raw_value']
        if 'Uyghur' not in ap['full_text']:
            continue
        al = []
        if 'extended_entities'in ap:
            ai=ap['extended_entities']
            if 'media' in ai:
                am=ai['media'][0]
                if 'ext' in am:
                    ar=am['ext']
                    if 'mediaStats' in ar:
                        ao=ar['mediaStats']
                        if 'r' in ao:
                            ak = ao['r']
                            if 'ok' in ak:
                                au = ak['ok']
                                if 'viewCount' in au:
                                    al = au['viewCount']
        else:
            k=0

        df=[]
        df.append(ap['user_id_str'])
        df.append(ap['id_str'])
        date_format = '%a %b %d %H:%M:%S %z %Y'
        date_time = datetime.strptime(ap['created_at'], date_format)
        date_format = '%Y-%m-%d %H:%M:%S'
        date_string = date_time.strftime(date_format)
        df.append(date_string)
        ac=[]
        if 'entities' in ap:
            ae=ap['entities']
            if 'media' in ae:
                aq=ae['media'][0]
                if 'url' in aq:
                    ac=aq['url']

        else:
            ab=ap['quoted_status_permalink']
            ac=ab['url']
        df.append(ac)
        df.append(ap['full_text'])
        df.append(ap['retweet_count'])
        df.append(ap['reply_count'])
        df.append(ap['quote_count'])
        df.append(ap['favorite_count'])
        df.append(al)
        dat.append(df)
df1 = pd.DataFrame(dat, columns=['发文用户id','推文id', '创建时间', '链接', '文本内容', '转发数量', '回复数量', '引用数量', '点赞数量', '浏览量'])
df1.drop_duplicates(subset='文本内容', keep='first', inplace=True)
with pd.ExcelWriter('my_list.xlsx', engine='xlsxwriter') as writer:
    df1.to_excel(writer, index=False)
with open('output_raw_search_users.jl','r') as f1:
    for line1 in f1:
        tweet1 = json.loads(line1)
        df2=[]
        ap1 = tweet1['raw_value']
        df2.append(ap1['id_str'])
        df2.append(ap1['screen_name'])
        df2.append(ap1['verified'])
        df2.append(ap1['name'])
        df2.append(ap1['location'])
        df2.append(ap1['description'])
        df2.append(ap1['normal_followers_count'])
        df2.append(ap1['friends_count'])
        date_format = '%a %b %d %H:%M:%S %z %Y'
        date_time = datetime.strptime(ap1['created_at'], date_format)
        date_format = '%Y-%m-%d %H:%M:%S'
        date_string = date_time.strftime(date_format)
        df2.append(date_string)
        df2.append(ap1['favourites_count'])
        df2.append(ap1['statuses_count'])
        df2.append(ap1['media_count'])
        dat1.append(df2)
df2 = pd.DataFrame(dat1, columns=['用户id','zhanghu','认证','用户名', '地址', '用户简介', '粉丝数', '好友数', '创建时间', '账户点赞数', '发文数量', '发表文件数'])
with pd.ExcelWriter('yonghu2.xlsx', engine='xlsxwriter') as writer:
    df2.to_excel(writer, index=False)