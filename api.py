#
# import tweepy
#
#
# # 填入你的 API 密钥和访问令牌
# consumer_key = 'EUB4twisUoWDQa5YaZA6gguwu'
# consumer_secret = 'oqKnbc1121tgaMhFD9aZVJlMBNCCehOXEXOjyD7nYtBE8QHhAh'
# access_token = '1641230400138915840-btIof24XimvItlYDvzfvbklLb124UF'
# access_token_secret = 'r92MIQ4zAZZ1zjoAKYHOZdvH1irpFp6woQtUhaUJfAVJE'
# #*处代表你自己的之前获得的四个参数
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
# tweets = api.user_timeline(id = 'realDonaldTrump',count = 10)
# for tweet in tweets:print(tweet.text)
#
# from TwitterAPI import TwitterAPI
# consumer_key = 'CkrkteKcSLX3FFiyqOoXAOkBK'
# consumer_secret = 'jBdabrt641Trc86Zb9cd7ZKbqbux4djSRsBngnP35NyDCdPdph'
# access_token = '1641230400138915840-YrIHVpj3Qi8R3diRs7mHGvCZHc7zRv'
# access_token_secret = 'DaUFGDTSLGg7c1uxrlTVQTCKbTP3enz6fl2OpWNcSbGfi'
# api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
# r = api.request('search/tweets', {'q': '关键词'})
# for tweet in r.get_iterator():
#     print(tweet['text'])
# -*- coding:utf-8 -*-
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def search_tweets(the_consumer_key, the_consumer_secret, the_access_token_key,
                  the_access_token_secret, the_proxy_url):
    """
    搜索含有特定“内容”的推文
    :param the_consumer_key: 已有的consumer_key
    :param the_consumer_secret: 已有的consumer_secret
    :param the_access_token_key: 已有的access_token_key
    :param the_access_token_secret: 已有的access_token_secret
    :param the_proxy_url: 代理及端口号
    :return:
    """
    api = TwitterAPI(consumer_key=the_consumer_key,
                     consumer_secret=the_consumer_secret,
                     access_token_key=the_access_token_key,
                     access_token_secret=the_access_token_secret,
                     proxy_url=the_proxy_url)

    r = TwitterPager(api, 'search/tweets', {'q': 'pizza', 'count': 10})
    for item in r.get_iterator():
        if 'text' in item:
            print(item['text'].encode('utf-8').decode('utf-8'))
        elif 'message' in item and item['code'] == 88:
            print('SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message'])
            break


if __name__ == "__main__":
    consumer_key = 'f61PJCitqx8YXwme4FgiFTJb9'
    consumer_secret = 'fC3olOE7YaBHF3ksI8KCpHwCmWuaIeimZwK2EmpQ1HzHSkaf1k'
    access_token = '1641230400138915840-5bTlqQChPSaRjUcSFPXwd4hdpkmzHS'
    access_token_secret = '3JHdtWJr40ercYDVRBQto5hsCG8DGUyWt9uv3MoWhqAeZ'
    proxyUrl = "https://12602:cmf030610@127.0.0.1:62533"  # 填写你的代理

    search_tweets(the_consumer_key=consumer_key,
                  the_consumer_secret=consumer_secret,
                  the_access_token_key=access_token,
                  the_access_token_secret=access_token_secret,
                  the_proxy_url=proxyUrl)