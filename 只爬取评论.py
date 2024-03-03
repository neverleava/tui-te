# import json
# import stweet as st
# import pandas as pd
# import xlwt
# import csv
# from datetime import datetime
# import time
# import jsonline
#
# def try_get_replies(tweet_id, output_file,k):
#     tweet_task = st.TweetsByIdTask(tweet_id)
#     output_json_tweet = st.JsonLineFileRawOutput(output_file)
#     output_print = st.PrintRawOutput()
#     tweet_runner = st.TweetsByIdRunner(tweets_by_id_task=tweet_task,
#                                         raw_data_outputs=[output_print, output_json_tweet])
#     tweet_runner.run()
#
# if __name__ == '__main__':
#     input_file1 = '推文ID.json'
#     output_file = 'output_raw_tweet.jl'
#     dat = []
#     counter = 1
#     with open(input_file1, 'r') as f1:
#         for line1 in f1:
#             tweet1 = json.loads(line1)
#             counter += 1
#             try_get_replies(tweet1, output_file,str(counter))
#
#
import tweepy

# 填入你的 Twitter API 访问令牌和密钥
API_KEY = "2LxGlhHmEivK3mFEIiV5yFKhxy"
API_SECRET = "GwXn4PJTdCUwrFp26S5GvliODZqgY3NuP8S0nucBUh9Mr1gEwz"
ACCESS_TOKEN = "1641230400138915840-MNf1GzZQtCkh3WSKXqDj9sPqlCWbaC"
ACCESS_TOKEN_SECRET = "59VFewhqIcpXDD5FJzFcI7IjXPiTnESbB3qZto6CUUJRX"

# 创建认证对象并设置 API 访问令牌
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# 创建 API 客户端
api = tweepy.API(auth)

# 设置搜索参数
mn = "Uyghur"
mnb = "2023-06-01"
mnc = "2023-06-30"

# 使用 API 客户端进行搜索
tweets = tweepy.Cursor(api.search_tweets, q=mn, lang="zh", since=mnb, until=mnc).items()

# 遍历搜索结果并处理推文
for tweet in tweets:
    # 处理每个推文的代码
    # 可以打印推文文本、作者等等
    print(tweet.text, tweet.user.screen_name)
