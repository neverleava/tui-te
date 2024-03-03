import requests

url = "/RPC_world_map"

try:
    print(2)
    response = requests.get(url)
    print(1)
    data_map = response.json()

    print("begin")
    print(data_map['dataAddr'])
    print(data_map['locations'])
    print("end")

    # 假设你在一个类中，且`that`是这个类的实例
    that.mapData['dataArr'] = data_map['dataAddr']
    that.mapData['locations'] = data_map['locations']
    that.isLoaded.map = True
    that.drawChart()

except requests.exceptions.RequestException:
    print("访问错误")
