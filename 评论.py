import tweepy

# 设置 Twitter API 访问凭据
# consumer_key = "xrsYRmhEH8GeYm4HVEgW3NNrP"
# consumer_secret = "sArlfNiFq0D1sqPQl05vwCUC3Du8ZkfEXryu8jwfWMGLY6bojp"
# access_token = "1641230400138915840-jH5F3U3c5eUC5x56Ayi6mOk66wnirH"
# access_token_secret = "Vvaj0LBTv1zfR1i5hyGJbubUUhdnkbnGdbEz1lEpyXpfH"
#
# import tweepy
#
# # 设置 API密钥 和 令牌
# auth = tweepy.OAuthHandler('f61PJCitqx8YXwme4FgiFTJb9', 'fC3olOE7YaBHF3ksI8KCpHwCmWuaIeimZwK2EmpQ1HzHSkaf1k')
# auth.set_access_token('1641230400138915840-5bTlqQChPSaRjUcSFPXwd4hdpkmzHS', '3JHdtWJr40ercYDVRBQto5hsCG8DGUyWt9uv3MoWhqAeZ')
#
# # 创建API对象
# api = tweepy.API(auth)
#
# # 要爬取的推文ID
# tweet_id = '1581453574332362752'
# print(1)
# # 获取推文的评论
# comments = api.get_status(tweet_id, tweet_mode='extended',user_auth=True)._json['retweeted_status']['full_text']
#
# # 打印所有评论
# for comment in comments:
#     print(comment['full_text'])
import tweepy

consumer_key = 'f61PJCitqx8YXwme4FgiFTJb9'
consumer_secret = 'fC3olOE7YaBHF3ksI8KCpHwCmWuaIeimZwK2EmpQ1HzHSkaf1k'
access_token = '1641230400138915840-5bTlqQChPSaRjUcSFPXwd4hdpkmzHS'
access_token_secret = '3JHdtWJr40ercYDVRBQto5hsCG8DGUyWt9uv3MoWhqAeZ'
auth = tweepy.OAuth1UserHandler(consumer_key=consumer_key,
                                    consumer_secret=consumer_secret,
                                    access_token=access_token,
                                    access_token_secret=access_token_secret)
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)
client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret,bearer_token='AAAAAAAAAAAAAAAAAAAAANtroAEAAAAAhR1z7vjMVwIPdnh1daQvhzhvNE0%3D918gXM6MZoKGij8JmXun0I5ZanQl1Q492TVn50Z0aTl17oV47F')
query = 'Uyghur'
tweets = client.search_all_tweets(query=query,end_time='2018-10-02T15:00:00Z',start_time = "2018-09-02T15:00:00Z",max_results=10, user_auth=True,limit=2)
for tweet in tweets.data:
    print(tweet.text)