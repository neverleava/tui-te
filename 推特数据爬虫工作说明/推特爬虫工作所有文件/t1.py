import snscrape.modules.twitter as sntwitter
import pandas as pd

# 搜索关键字
search_words = "#Uyghur"

# 设置日期范围
since_date = "2020-01-01"
until_date = "2023-03-31"

# 构建查询语句
query = f"{search_words}"

# 执行查询
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    tweets.append([tweet.date, tweet.id, tweet.content])

# 将结果保存到CSV文件
df = pd.DataFrame(tweets, columns=["Datetime", "Tweet Id", "Text"])
df.to_csv("tweets.csv", index=False)
