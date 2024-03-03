import twint

# 创建一个配置对象
c = twint.Config()

# 设置搜索关键字
c.Search = "关键字"

# 设置要爬取的用户的用户名
# 如果要爬取所有用户相关的推文，可以注释掉这一行
c.Username = "用户名"

# 设置开始和结束日期（可选）
# 格式：YYYY-MM-DD
c.Since = "2022-01-01"
c.Until = "2022-01-31"

# 设置要爬取的推文数量（可选）
c.Limit = 100

# 设置输出格式为CSV（可选）
c.Store_csv = True
c.Output = "tweets.csv"

# 运行爬虫
twint.run.Search(c)
