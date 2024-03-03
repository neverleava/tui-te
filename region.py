import requests
import pandas as pd

excel_file_path = "twarc\cleaned.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

df["location"] = ""
df["addr"] = ""

for index,row in df.iterrows():
    region = row['author.location']

    if pd.isna(region):
        location_result = "-"
        addr_result = "-"

    else:       
        url = "http://118.89.122.209:8001/get_count_loc"
        params = {"region": region}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) == 2 and isinstance(data[1], list):
                addr_result = data[0]
                location_result = "({:.6f}, {:.6f})".format(data[1][0], data[1][1])
    df.at[index,"location"] = location_result
    df.at[index,"addr"] = addr_result

df.to_excel(excel_file_path, index=False)
