import stweet as st
import os
import arrow
from datetime import datetime, timedelta
import json
import pandas as pd
import xlwt
import csv
from datetime import datetime
import numpy as np

def try_search(tag,sy,sm,sd,ey,em,ed,theme):
    if tag==0:
        start_date = datetime(sy, sm, sd)
        end_date = datetime(ey, em, ed)
        current_date = start_date
    else:
        # 获取当前日期
        current_date = datetime.now().date()
        # 获取前一日日期
        previous_date = current_date - timedelta(days=1)
        # 将日期转换为指定格式的字符串
        current_date = current_date.strftime("%Y, %-m, %-d")
        end_date = previous_date.strftime("%Y, %-m, %-d")
    while current_date <= end_date:
        current_date.strftime("%Y-%m-%d")
        c1=current_date+timedelta(days=1)
        since1 = arrow.get(current_date)
        until1 = arrow.get(c1)
        search_tweets_task = st.SearchTweetsTask(all_words=theme,since=since1, until=until1)
        output_jl_tweets = st.JsonLineFileRawOutput('output_raw_search_tweets.jl')
        output_jl_users = st.JsonLineFileRawOutput('output_raw_search_users.jl')
        output_print = st.PrintRawOutput()
        st.TweetSearchRunner(search_tweets_task=search_tweets_task,
                             tweet_raw_data_outputs=[output_print, output_jl_tweets],
                             user_raw_data_outputs=[output_print, output_jl_users]).run()
        current_date += timedelta(days=1)

def try_user_scrap():
    user_task = st.GetUsersTask(["Kalbinur Gheni"])
    output_json = st.JsonLineFileRawOutput('C:/Users/12602/Desktop/output_raw_user.jl')
    output_print = st.PrintRawOutput()
    st.GetUsersRunner(get_user_task=user_task, raw_data_outputs=[output_print, output_json]).run()
#
#
def try_tweet_by_id_scrap():
    id_task = st.TweetsByIdTask('1188315702316417029')
    output_json = st.JsonLineFileRawOutput('output_raw_id.jl')
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(tweets_by_id_task=id_task,
                        raw_data_outputs=[output_print, output_json]).run()
def try_get_replies(tweet_id):
    tweet_task = st.TweetsByIdTask(tweet_id)
    output_json_tweet = st.JsonLineFileRawOutput('output_raw_tweet.jl')

    output_print = st.PrintRawOutput()
    tweet_runner = st.TweetsByIdRunner(tweets_by_id_task=tweet_task,
                                        raw_data_outputs=[output_print, output_json_tweet])
    tweet_runner.run()
def w():
    dat = []
    dat1 = []
    with open('output_raw_search_tweets.jl', 'r') as f:
        for line in f:
            tweet = json.loads(line)
            ap = tweet['raw_value']
            if 'Uyghur' not in ap['full_text']:
                continue
            al = []
            if 'extended_entities' in ap:
                ai = ap['extended_entities']
                if 'media' in ai:
                    am = ai['media'][0]
                    if 'ext' in am:
                        ar = am['ext']
                        if 'mediaStats' in ar:
                            ao = ar['mediaStats']
                            if 'r' in ao:
                                ak = ao['r']
                                if 'ok' in ak:
                                    au = ak['ok']
                                    if 'viewCount' in au:
                                        al = au['viewCount']
            else:
                k = 0

            df = []
            df.append(ap['user_id_str'])
            df.append(ap['id_str'])
            date_format = '%a %b %d %H:%M:%S %z %Y'
            date_time = datetime.strptime(ap['created_at'], date_format)
            date_format = '%Y-%m-%d %H:%M:%S'
            date_string = date_time.strftime(date_format)
            df.append(date_string)
            ac = []
            if 'entities' in ap:
                ae = ap['entities']
                if 'media' in ae:
                    aq = ae['media'][0]
                    if 'url' in aq:
                        ac = aq['url']

            else:
                ab = ap['quoted_status_permalink']
                ac = ab['url']
            df.append(ac)
            df.append(ap['full_text'])
            df.append(ap['retweet_count'])
            df.append(ap['reply_count'])
            df.append(ap['quote_count'])
            df.append(ap['favorite_count'])
            df.append(al)
            dat.append(df)
    df1 = pd.DataFrame(dat, columns=['发文用户id', '推文id', '创建时间', '链接', '文本内容', '转发数量', '回复数量',
                                     '引用数量', '点赞数量', '浏览量'])
    df1.drop_duplicates(subset='文本内容', keep='first', inplace=True)
    with pd.ExcelWriter('my_list.xlsx', engine='xlsxwriter') as writer:
        df1.to_excel(writer, index=False)
    with open('output_raw_search_users.jl', 'r') as f1:
        for line1 in f1:
            tweet1 = json.loads(line1)
            df2 = []
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
    df2 = pd.DataFrame(dat1, columns=['用户id', 'zhanghu', '认证', '用户名', '地址', '用户简介', '粉丝数', '好友数',
                                      '创建时间', '账户点赞数', '发文数量', '发表文件数'])
    with pd.ExcelWriter('yonghu2.xlsx', engine='xlsxwriter') as writer:
        df2.to_excel(writer, index=False)
def reply():
    input_file = 'output_raw_tweet.jl'
    dat = []
    d = pd.read_excel('tuiwen(只包含推文ID，链接，文本内容).xlsx', usecols=[0, 1, 2])
    for index, row in d.iterrows():
            tweet1 = row[0]

            tweet2 = row[1]
            tweet3 = row[2]
            try_get_replies(tweet1)
            df=[]
            with open(input_file, 'r', encoding='utf-8') as f_in:
                # 遍历输入文件中的每一行
                for line in f_in:
                    # 将每一行的 JSON 字符串转换为 Python 字典
                    data = json.loads(line)
                    df = []
                    df.append(str(tweet1))
                    df.append(tweet2)
                    df.append(tweet3)
                    # 从字典中获取特定项的值
                    text = data['raw_value']
                    t1 = []
                    t8 = []
                    t9 = []
                    if 'legacy' in text:
                        t1 = text['legacy']
                        t2 = t1['full_text']
                        t8 = t1['entities']
                        t9 = t8['user_mentions']
                    if 'core' in text:
                        t3 = text['core']
                        t4 = t3['user_results']
                        t5 = t4['result']
                        t6 = t5['legacy']

                    t97 = []
                    t98 = []
                    if len(t9) == 0:
                        t96 = []
                    else:
                        t96 = t9[0]
                        t97 = t96['id_str']
                        t98 = t96['name']
                    t45 = []
                    t46 = []
                    date_string = ''
                    t48 = []
                    t49 = []
                    t50 = []
                    t51 = []
                    if 'location' in t6 and 'statuses_count' in t6 and 'created_at' in t1 and 'favorite_count' in t1 and 'quote_count' in t1 and 'reply_count' in t1 and 'retweet_count' in t1:
                        t45 = t6['location']
                        t46 = t6['statuses_count']
                        t47 = t1['created_at']
                        t48 = t1['favorite_count']
                        t49 = t1['quote_count']
                        t50 = t1['reply_count']
                        t51 = t1['retweet_count']
                        date_format = '%a %b %d %H:%M:%S %z %Y'
                        date_time = datetime.strptime(t47, date_format)
                        date_format = '%Y-%m-%d %H:%M:%S'
                        date_string = date_time.strftime(date_format)
                    df.append(t45)
                    df.append(t46)
                    df.append(date_string)
                    df.append(t97)
                    df.append(t98)
                    df.append(t2)
                    df.append(t48)
                    df.append(t49)
                    df.append(t50)
                    df.append(t51)
                    dat.append(df)
            with open(input_file, 'w') as f6:
                f6.truncate(0)
            # print(dat)
    # with open('tweets.csv', 'w', encoding='utf-8',newline='') as f2:
    #     writer = csv.writer(f2)
    #     writer.writerow(['推文id', '创建时间', '链接', '文本内容', '转发数量', '回复数量', '引用数量', '点赞数量', '浏览量', '用户名', '地址', '用户简介', '粉丝数', '好友数', '创建时间', '账户点赞数', '发文数量', '发表文件数', '评论地址','评论人发文数','评论时间','评论人id','评论人名字','评论内容','评论点赞数','评论引用数','评论回复数','评论转发数'])
    #     writer.writerows(dat)
    df1 = pd.DataFrame(dat, columns=['推文id','链接', '文本内容', '评论地址','评论人发文数','评论时间','评论人id','评论人名字','评论内容','评论点赞数','评论引用数','评论回复数','评论转发数'])
    with pd.ExcelWriter('pinglun3.xlsx', engine='xlsxwriter') as writer:
        df1.to_excel(writer, index=False)

    # print(ap['id_str'])
            # print(ap['full_text'])
if __name__ == '__main__':
    tag=0#0代表更新，其余代表指定日期
    sy=2023
    sm=4
    sd=30
    ey=2023
    em=5
    ed=2
    theme='Uyghur'
    try_search(tag,sy,sm,sd,ey,em,ed,theme)
    w()
    reply()