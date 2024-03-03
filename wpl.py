import json
import stweet as st
import pandas as pd
import xlwt
import csv

from datetime import datetime
input_file = 'output_raw_tweet.jl'
dat=[]
with open(input_file, 'r', encoding='utf-8') as f_in:
    # 遍历输入文件中的每一行
    for line in f_in:
        # 将每一行的 JSON 字符串转换为 Python 字典
        data = json.loads(line)
        df=[]
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
        t45=[]
        t46=[]
        date_string=''
        t48=[]
        t49=[]
        t50=[]
        t51=[]
        if 'location' in t6 and 'statuses_count' in t6 and 'created_at' in t1 and 'favorite_count' in t1 and 'quote_count' in t1 and 'reply_count' in t1 and 'retweet_count' in t1:
            t45=t6['location']
            t46=t6['statuses_count']
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
df1 = pd.DataFrame(dat, columns=['评论地址','评论人发文数','评论时间','评论人id','评论人名字','评论内容','评论点赞数','评论引用数','评论回复数','评论转发数'])
# df1.drop_duplicates(subset='评论内容', keep='first', inplace=True)
with pd.ExcelWriter('pinglun.xlsx', engine='xlsxwriter') as writer:
    df1.to_excel(writer, index=False)