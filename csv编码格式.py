import csv

# 打开CSV文件
with open('C:/Users/21839/One_Belt_One_Road.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # 获取文件编码格式
    encoding = csvfile.encoding
    print("文件编码格式为：" + encoding)