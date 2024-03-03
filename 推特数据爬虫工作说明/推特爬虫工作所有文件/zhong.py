import pandas as pd

# 读取 Excel 表格
df = pd.read_excel('my_list1 - 副本.xlsx')

# 统计某一列每一种出现的次数，并添加到新的一列中
df['发文数量'] = df['用户id'].apply(lambda x: df['用户id'].tolist().count(x))

# 写入 Excel 表格
df.to_excel('my_list1 - 副本.xlsx', index=False)
