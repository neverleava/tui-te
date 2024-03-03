import pandas as pd
import os
import subprocess
import requests
import schedule


def getemotion(excel_file_path,sheet_name):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    df["emotion"] = ""
    for index, row in df.iterrows():
        sentence = row['text']
        if pd.isna(sentence):
            result = "[-,-]"
        else:
            url = "http://10.126.62.38:9001//getEmotion"
            params = {"sentence": sentence}
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and len(data) == 2 and isinstance(data[1], list):
                    result = data[0]
        df.at[index, "emotion"] = result
    df.to_excel(excel_file_path, index=False)
def getsentiment(excel_file_path,sheet_name):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    df["sentiment"] = ""
    for index, row in df.iterrows():
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
        df.at[index, "sentiment"] = result
    df.to_excel(excel_file_path, index=False)
def region(excel_file_path,sheet_name):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    df["location"] = ""
    df["addr"] = ""
    for index, row in df.iterrows():
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
        df.at[index, "location"] = location_result
        df.at[index, "addr"] = addr_result
    df.to_excel(excel_file_path, index=False)

def processing(csv_file_path, xlsx_file):
    def run_command_in_cmd(command, working_directory):
        try:
            subprocess.run( command, shell=True, check=True, cwd=working_directory)
        except subprocess.CalledProcessError as e:
            print(f"命令执行失败：{e}")
        except Exception as e:
            print(f"发生错误：{e}")


    def remove_duplicates_from_csv(csv_file, column_name):
        encoding_formats = ['utf8']
        for encoding_format in encoding_formats:
            try:
                df = pd.read_csv(csv_file, encoding=encoding_format)
                break
            except UnicodeDecodeError:
                continue
            except Exception as e:
                print(f"尝试使用 {encoding_format} 编码读取时发生错误: {e}")
        columns_to_keep = ['id', 'conversation_id', 'referenced_tweets.replied_to.id', 'referenced_tweets.retweeted.id', 'referenced_tweets.quoted.id', 'author_id', 'in_reply_to_user_id', 'in_reply_to_username', 'retweeted_user_id', 'retweeted_username', 'quoted_user_id', 'quoted_username', 'created_at', 'text', 'lang', 'source', 'public_metrics.impression_count', 'public_metrics.reply_count', 'public_metrics.retweet_count', 'public_metrics.quote_count', 'public_metrics.like_count', 'public_metrics.bookmark_count', 'reply_settings', 'edit_history_tweet_ids', 'edit_controls.edits_remaining', 'edit_controls.editable_until', 'edit_controls.is_edit_eligible', 'possibly_sensitive', 'withheld.scope', 'withheld.copyright', 'withheld.country_codes', 'entities.annotations', 'entities.cashtags', 'entities.hashtags', 'entities.mentions', 'entities.urls', 'context_annotations', 'attachments.media', 'attachments.media_keys', 'attachments.poll.duration_minutes', 'attachments.poll.end_datetime', 'attachments.poll.options', 'attachments.poll.voting_status', 'attachments.poll_ids', 'author.id', 'author.created_at', 'author.username', 'author.name', 'author.description', 'author.entities.description.cashtags', 'author.entities.description.hashtags', 'author.entities.description.mentions', 'author.entities.description.urls', 'author.entities.url.urls', 'author.url', 'author.location', 'author.pinned_tweet_id', 'author.profile_image_url', 'author.protected', 'author.public_metrics.followers_count', 'author.public_metrics.following_count', 'author.public_metrics.listed_count', 'author.public_metrics.tweet_count', 'author.verified', 'author.verified_type', 'author.withheld.scope', 'author.withheld.copyright', 'author.withheld.country_codes', '__twarc.retrieved_at', '__twarc.url', '__twarc.version']
        df = df[columns_to_keep]
        df.drop_duplicates(subset=[column_name], keep='first', inplace=True)
        return df

    def convert_csv_to_xlsx(csv_file_path, xlsx_file):
        column_to_remove_duplicates = 'text'
        cleaned_df = remove_duplicates_from_csv(csv_file_path, column_to_remove_duplicates)
        cleaned_df.to_excel(xlsx_file, index=False)

    def remove_garbled_characters(file_path):
        df = pd.read_excel(file_path)
        id_column=[]
        if 'id' in df.columns:
            id_column = df['id'].copy()
            df.drop(columns=['id'], inplace=True)
        id_column1 = []
        if 'conversation_id' in df.columns:
            id_column1 = df['conversation_id'].copy()
            df.drop(columns=['conversation_id'], inplace=True)
        df = df.astype(str)
        df.replace("nan", "", inplace=True)
        df["text"] = df["text"].str.replace("http[s]?://[^\s]*", "", regex=True)  # 去掉URL
        df["text"] = df["text"].str.replace("\n", " ", regex=True)  # 去掉换行符（使用原始字符串）
        df["text"] = df["text"].str.replace("@[^ ]*", "@Users", regex=True)  # 替换@后面的字符串为"Users"
        df = df[df["text"].str.contains("Tibet|Uyghur|tibet|uyghur|One Belt One Road")]

        contains_special_characters = df.apply(lambda row: any(
            "ð" in cell or "æ" in cell or "Ø" in cell or "âï" in cell or "Â" in cell or "å" in cell or "â" in cell or "¤" in cell or "Ã" in cell or "Ä" in cell or "à" in cell or "å" in cell or "ä" in cell or "è" in cell or "ë" in cell or "Ð" in cell or "Ñ" in cell
            for cell in row), axis=1)
        df = df[~contains_special_characters]
        df.drop_duplicates(subset=["text"], keep='first', inplace=True)
        if id_column is not None:
            df = pd.concat([id_column, df], axis=1)
        if id_column1 is not None:
            df = pd.concat([id_column1, df], axis=1)
        df = df[df['text'].notna()]
        return df

    def runn():

        command_to_run1 = r"twarc2 search 'Uyghur' Uyghur.jsonl"
        command_to_run = r"twarc2 csv Uyghur.jsonl Uyghur.csv"
        working_directory = r"C:\Users\12602"
        run_command_in_cmd(command_to_run1, working_directory)
        run_command_in_cmd(command_to_run, working_directory)

    # runn()
    convert_csv_to_xlsx(csv_file_path, xlsx_file)
    cleaned_df = remove_garbled_characters(xlsx_file)
    cleaned_df.to_excel(xlsx_file, index=False)
if __name__ == "__main__":
    csv_file_path = 'C:/Users/21839/One_Belt_One_Road.csv'  # 替换成你的CSV文件路径
    xlsx_file = "One_Belt_One_Road.xlsx"
    processing(csv_file_path, xlsx_file)
    getemotion(xlsx_file,"Sheet1")
    getsentiment(xlsx_file,"Sheet1")
    region(xlsx_file,"Sheet1")
    # schedule.every(6).days.do(processing(csv_file_path, xlsx_file))
    # while True:
    #     schedule.run_pending()

