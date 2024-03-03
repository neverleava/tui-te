from flask import Flask, render_template, request
import pandas as pd
import arrow
import stweet as st
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<html>
<head>
    <title>按钮和输入框示例</title>
</head>
<body>
    <button onclick="executeFunction(1)">更新</button>
    <button onclick="executeFunction(2)">查看当日数据</button>
    <button onclick="executeFunction(3)">查看历史数据</button>
    <button onclick="executeFunction(4)">重新爬取</button>
    <button onclick="executeFunction(5)">关闭</button>

    <script>
        function executeFunction(buttonId) {
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "/execute/" + buttonId, true);
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    alert("函数执行成功！");
                }
            };
            xhr.send();
        }
    </script>
    <form action="/process" method="POST">
        <input type="text" name="input1" placeholder="输入关键词"><br>
        <input type="text" name="input2" placeholder="输入起始日期"><br>
        <input type="text" name="input3" placeholder="输入截止日期"><br>
    </form>
</body>
</html>
'''
#从since-until这段时间里爬取所有含关键词的推文
def try_search():
    since1=arrow.get('2023-04-01')
    until1=arrow.get('2023-04-02')
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


@app.route('/process', methods=['POST'])
def process():
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']

    # 执行相应的函数，处理输入的字符串（示例中仅打印输入的值）
    print("输入1：", input1)
    print("输入2：", input2)
    print("输入3：", input3)

    # 读取 Excel 表格并将内容转换为 HTML 表格
    df = pd.read_excel('yonghu1.xlsx')
    html_table = df.to_html(index=False)

    return '''<html>
<head>
    <title>结果页面</title>
</head>
<body>
    <h2>执行结果：</h2>
    {{ table|safe }}
</body>
</html>'''
@app.route('/execute/<int:button_id>')
def execute_function(button_id):
    # 根据按钮的 ID 执行相应的函数
    if button_id == 1:
        function1()
    elif button_id == 2:
        function2()
    elif button_id == 3:
        function3()
    elif button_id == 4:
        function4()
    elif button_id == 5:
        function5()

    return 'Success'

def function1():
    try_search()
    pass

def function2():
    # 在这里定义按钮 2 对应的函数逻辑
    pass

def function3():
    # 在这里定义按钮 3 对应的函数逻辑
    pass

def function4():
    # 在这里定义按钮 4 对应的函数逻辑
    pass

def function5():
    # 在这里定义按钮 5 对应的函数逻辑
    pass

if __name__ == '__main__':
    app.run()
