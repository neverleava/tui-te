import stweet as st

# 创建一个SearchTweetsIterable对象
search_tweets_iterable = st.SearchTweetsIterable(
    query='1529662469710480000',
    lang='en'
)

# 获取第一条结果的推文id
tweet_id = search_tweets_iterable.get_tweets_list()[0].id

# 获取推文的评论
comments = st.get_tweet_comments(tweet_id)

# 打印评论
for comment in comments:
    print(comment.text)
