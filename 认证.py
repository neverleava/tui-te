# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# import pandas as pd
# # 创建 Chrome WebDriver 实例并打开 Twitter 主页
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# # 创建 Chrome WebDriver 实例并打开 Twitter 主页
# driver = webdriver.Chrome()
# driver.get("https://twitter.com/")
#
# # 找到搜索框并输入用户名
# search_box = driver.find_element_by_name("q")
# search_box.send_keys("username") # 这里的 "username" 需要替换为您要搜索的用户名
#
# # 按下回车键以提交搜索请求
# search_box.send_keys(Keys.RETURN)
#
# # 等待页面加载完成
# time.sleep(5)
#
# # 关闭浏览器窗口
# driver.quit()
#
# df =pd.read_excel("yonghu2.xlsx",header=0)
# dat=[]
# for f in df['zhanghu']:
#     str="https://twitter.com/"+f
#     driver = webdriver.Chrome('D:/程序/python/venv/chromedriver.exe')
#     driver.get(str)
#     # 找到搜索框并输入用户名
#     try:
#         s=driver.find_element(By.XPATH, '//*[@class="css-18t94o4 css-1dbjc4n r-6koalj r-9cviqr r-1ny4l3l r-o7ynqc r-6416eg"]').click()
#         # css-18t94o4 css-1dbjc4n r-6koalj r-9cviqr r-1ny4l3l r-o7ynqc r-6416eg
#         dat.append("是")
#         print("+v")
#         # 等待页面加载完成
#         time.sleep(0)
#         driver.quit()
#     except:
#         print("no+v")
#         dat.append("否")
#         driver.quit()
#         continue
# df1=pd.DataFrame(dat,columns=['是否+v'])
# df['是否+v']=df1
# df.to_excel('example_with_new_data.xlsx', index=False)
# # <selenium.webdriver.remote.webelement.WebElement (session="9f135f84e8d51e5e2fa1993ae8cda6ce", element="A0B906E32FF6E392B879E4622314EA68_element_42")>
#
# # import requests
# # from bs4 import BeautifulSoup
# #
# # # 获取推特账号页面信息
# # url = "https://twitter.com/Qelbinur10"
# # response = requests.get(url)
# # soup = BeautifulSoup(response.text, "html.parser")
# # # print(response.text)
# # # 查找包含蓝V标识的元素
# # verified_element = soup.find("div", {"aria-label": "Provides details about verified accounts."})
# #
# # # 判断是否包含蓝V标识
# # if verified_element:
# #     print("该账号为蓝V账号")
# # else:
# #     print("该账号不是蓝V账号")
# import stweet as st
# # import tweepy
# #
# # # 填写Twitter开发者账号的API Key和API Secret
# # auth = tweepy.OAuthHandler("4om4GUpFR3Zxz4BV0N7t1aETo", "DkGQapaPv0CFtg3hGzgbtJUd0lzOLsSJGBgkB4HvqS3UnKaRJ2")
# # auth.set_access_token("1641230400138915840-yxEZZG7QukmheWHEPqzVzy5gtNacoh", "KRhq7LqPrwsSuBfTTAOvyoDJ2Natd7Y1aDfjcQeAFpVQ7")
# #
# # # 创建API对象
# # api = tweepy.API(auth)
# #
# # # 用户名
# # user1 = "Russia 🇷🇺"
# # user2 = "MFA Russia 🇷🇺"
# #
# # # 判断两个用户是否互相关注
# # friendship = api.get_friendship(source_id="343627165", target_id="34613288")
# # if friendship[0].following and friendship[1].following:
# #     print(f"{user1}和{user2}互相关注")
# # else:
# #     print(f"{user1}和{user2}没有互相关注")
# # import stweet as st
# # search_tweets_task = st.SearchTweetsTask(from_username='Arsenal',to_username='Premier League',tweets_limit=10)
# # output_jl_tweets = st.JsonLineFileRawOutput('output_raw_search_tweets.jl')
# # output_jl_users = st.JsonLineFileRawOutput('output_raw_search_users.jl')
# # output_print = st.PrintRawOutput()
# # st.TweetSearchRunner(search_tweets_task=search_tweets_task,
# #                      tweet_raw_data_outputs=[output_print, output_jl_tweets],
# #                      user_raw_data_outputs=[output_print, output_jl_users]).run()





from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('D:/程序/python/venv/chromedriver.exe')  # 使用Chrome浏览器，需安装Chrome驱动并将其路径添加到系统环境变量中
driver.get("https://twitter.com")
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log in")))
login_button.click()
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "session[username_or_email]")))
password_input = driver.find_element(By.NAME, "session[password]")

username_input.send_keys("NLeave17581")  # 替换为您的用户名
password_input.send_keys("cmf030610")  # 替换为您的密码

password_input.send_keys(Keys.ENTER)  # 模拟按下回车键登录
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search query"]')))
search_input.send_keys("LNstats")  # 替换为要搜索的用户名
search_input.send_keys(Keys.ENTER)  # 模拟按下回车键进行搜索
