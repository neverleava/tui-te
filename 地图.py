import pandas as pd
import googlemaps
import plotly.express as px

# 输入您的Google Maps API密钥
gmaps = googlemaps.Client(key='AIzaSyCEqdzQwqbUy4q3bA4834T5siuYnM8RlWg')

# 读取位置名字所在的txt文件
df = pd.read_excel('用户.xlsx')

# 创建一个字典，存储每个国家的用户数量
country_dict = {}
df['地址']=df['地址'].astype(str)
# 遍历每个位置，根据位置名字获取其经纬度和所在国家，并进行统计
for location in df['地址']:
    # 获取该位置的经纬度和国家信息
    geocode_result = gmaps.geocode(location)
    if len(geocode_result) > 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        country = None
        for component in geocode_result[0]['address_components']:
            if 'country' in component['types']:
                country = component['long_name']
                break
        # 如果该位置在某个国家，则将该国家的用户数量加1
        if country:
            if country in country_dict:
                country_dict[country] += 1
            else:
                country_dict[country] = 1

# 将国家和用户数量存储到一个DataFrame中
country_df = pd.DataFrame.from_dict(country_dict, orient='index', columns=['users'])
country_df = country_df.reset_index().rename(columns={'index': 'country'})

# 画地图并染色
fig = px.choropleth(country_df, locations='country', locationmode='country names', color='users',
                    range_color=(0, country_df['users'].max()), color_continuous_scale='blues',
                    title='世界各国用户数量')
fig.show()
