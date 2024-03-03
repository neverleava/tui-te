import arrow
import stweet as st
import json
import pandas as pd
import xlwt
import csv
from datetime import datetime
#从since-until这段时间里爬取所有含关键词的推文
def try_search():
    since1=arrow.get('2023-04-01')
    until1=arrow.get('2023-04-05')
    search_tweets_task = st.SearchTweetsTask(all_words='#Uyghur',since=since1,until=until1)
    output_jl_tweets = st.JsonLineFileRawOutput('output_raw_search_tweets.jl')
    output_jl_users = st.JsonLineFileRawOutput('output_raw_search_users.jl')
    output_print = st.PrintRawOutput()
    st.TweetSearchRunner(search_tweets_task=search_tweets_task,
                         tweet_raw_data_outputs=[output_print, output_jl_tweets],
                         user_raw_data_outputs=[output_print, output_jl_users]).run()

#根据用户的username来查找对应含关键词的推文
def try_user_scrap():
    user_task = st.GetUsersTask(['iga_swiatek'])
    output_json = st.JsonLineFileRawOutput('output_raw_user.jl')
    output_print = st.PrintRawOutput()
    st.GetUsersRunner(get_user_task=user_task, raw_data_outputs=[output_print, output_json]).run()

#获取相应的推文ID对应的推文
def try_tweet_by_id_scrap():
    id_task = st.TweetsByIdTask('1447348840164564994')
    output_json = st.JsonLineFileRawOutput('output_raw_id.jl')
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(tweets_by_id_task=id_task,
                        raw_data_outputs=[output_print, output_json]).run()

if __name__ == '__main__':
    try_search()
    # try_user_scrap()
    # try_tweet_by_id_scrap()