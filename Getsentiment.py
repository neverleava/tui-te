import requests
import pandas as pd

excel_file_path = "twarc\cleaned.xlsx"
sheet_name = "Sheet1"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

df["sentiment"] = ""

for index,row in df.iterrows():
    sentence = row['text']

    if pd.isna(sentence):
        result = "-"

    else:       
        url = "http://10.126.62.38:9001//getSentiment"
        params = {"sentence": sentence}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) == 2 and isinstance(data[1], list):
                result = data[0]
    df.at[index,"sentiment"] = result

df.to_excel(excel_file_path, index=False)