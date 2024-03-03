# import pandas as pd
# import os
# import subprocess
#
# def run_command_in_cmd(command, working_directory):
#     try:
#         subprocess.run( command, shell=True, check=True, cwd=working_directory)
#     except subprocess.CalledProcessError as e:
#         print(f"命令执行失败：{e}")
#     except Exception as e:
#         print(f"发生错误：{e}")
#
#
# def remove_duplicates_from_csv(csv_file, column_name):
#     # 尝试不同的编码格式来读取CSV文件
#     encoding_formats = ['latin-1']
#     for encoding_format in encoding_formats:
#         try:
#             df = pd.read_csv(csv_file, encoding=encoding_format)
#             # 成功读取文件则跳出循环
#             break
#         except UnicodeDecodeError:
#             continue
#         except Exception as e:
#             print(f"尝试使用 {encoding_format} 编码读取时发生错误: {e}")
#
#     # 删除除了指定列之外的所有列
#     columns_to_keep = ['id', 'conversation_id', 'referenced_tweets.replied_to.id', 'referenced_tweets.retweeted.id',
#                        'referenced_tweets.quoted.id', 'author_id', 'in_reply_to_user_id', 'in_reply_to_username',
#                        'retweeted_user_id', 'retweeted_username', 'quoted_user_id', 'quoted_username', 'created_at',
#                        'text', 'lang', 'source', 'public_metrics.impression_count', 'public_metrics.reply_count',
#                        'public_metrics.retweet_count', 'public_metrics.quote_count', 'public_metrics.like_count',
#                        'public_metrics.bookmark_count', 'reply_settings', 'edit_history_tweet_ids',
#                        'edit_controls.edits_remaining', 'edit_controls.editable_until',
#                        'edit_controls.is_edit_eligible', 'possibly_sensitive', 'withheld.scope', 'withheld.copyright',
#                        'withheld.country_codes', 'entities.annotations', 'entities.cashtags', 'entities.hashtags',
#                        'entities.mentions', 'entities.urls', 'context_annotations', 'attachments.media',
#                        'attachments.media_keys', 'attachments.poll.duration_minutes', 'attachments.poll.end_datetime',
#                        'attachments.poll.options', 'attachments.poll.voting_status', 'attachments.poll_ids',
#                        'author.id', 'author.created_at', 'author.username', 'author.name', 'author.description',
#                        'author.entities.description.cashtags', 'author.entities.description.hashtags',
#                        'author.entities.description.mentions', 'author.entities.description.urls',
#                        'author.entities.url.urls', 'author.url', 'author.location', 'author.pinned_tweet_id',
#                        'author.profile_image_url', 'author.protected', 'author.public_metrics.followers_count',
#                        'author.public_metrics.following_count', 'author.public_metrics.listed_count',
#                        'author.public_metrics.tweet_count', 'author.verified', 'author.verified_type',
#                        'author.withheld.scope', 'author.withheld.copyright', 'author.withheld.country_codes',
#                        '__twarc.retrieved_at', '__twarc.url', '__twarc.version']
#
#     df = df[columns_to_keep]
#
#     # 根据指定的列名(column_name)，删除重复项及其所在的行
#     df.drop_duplicates(subset=[column_name], keep='first', inplace=True)
#
#     return df
#
# def convert_csv_to_xlsx(df, xlsx_file):
#     # 将数据写入到XLSX文件中
#     df.to_excel(xlsx_file, index=False)
#
# def remove_garbled_characters(file_path):
#     # 使用pandas库读取Excel文件
#     df = pd.read_excel(file_path)
#     # 将所有数据转换为字符串类型
#     df = df.astype(str)
#     # 将所有"nan"字符串替换为空字符串
#     df.replace("nan", "", inplace=True)
#     # 处理文本列
#     df["text"] = df["text"].str.replace("http[s]?://[^\s]*", "", regex=True)  # 去掉URL
#     df["text"] = df["text"].str.replace("\n", " ", regex=True)  # 去掉换行符（使用原始字符串）
#     df["text"] = df["text"].str.replace("@[^ ]*", "@Users", regex=True)  # 替换@后面的字符串为"Users"
#     df = df[df["text"].str.contains("Tibet|Uyghur|tibet|uyghur")]
#     # 针对每一列应用处理乱码的操作
#     for column in df.columns:
#         df[column] = df[column].apply(lambda x: x.encode('utf-8').decode('utf-8', 'ignore'))
#
#     # 将所有列的数据类型转换为字符串类型
#     df = df.astype(str)
#
#     # # 判断每个单元格是否包含"ð"或"æ"
#     # contains_special_characters = df.apply(lambda row: any("ð" in cell or "æ" in cell or "Ø" in cell or "âï" in cell or "Â" in cell or "å" in cell or "â" in cell or "¤" in cell or "Ã" in cell or "Ä" in cell or "à" in cell or "å" in cell or "ä" in cell or "è" in cell or "ë" in cell or "Ð" in cell or "Ñ" in cell for cell in row ), axis=1)
#     #
#     # # 通过布尔索引筛选出不包含特殊字符的行
#     # df = df[~contains_special_characters]
#     # df.drop_duplicates(subset=["text"], keep='first', inplace=True)
#     return df
#
# def runn():
#     # 要执行的命令
#     command_to_run1 = r"twarc2 search 'Uyghur' Uyghur.jsonl"
#     command_to_run = r"twarc2 csv Uyghur.jsonl Uyghur.csv"
#     # 要执行命令的工作目录
#     working_directory = r"C:\Users\12602"
#
#     # 调用函数打开命令行窗口并执行命令
#     run_command_in_cmd(command_to_run1, working_directory)
#
#     run_command_in_cmd(command_to_run, working_directory)
#
# if __name__ == "__main__":
#     # runn()
#     csv_file_path = 'C:/Users/12602/Tibet.csv'  # 替换成你的CSV文件路径
#     column_to_remove_duplicates = 'text'  # 替换成你想要删除重复项的列名
#
#     # 步骤一：移除重复项并保存为DataFrame
#     cleaned_df = remove_duplicates_from_csv(csv_file_path, column_to_remove_duplicates)
#
#     # 步骤二：将DataFrame转换为XLSX文件并保存
#     xlsx_file = "TIBET.xlsx"
#     convert_csv_to_xlsx(cleaned_df, xlsx_file)
#
#     # 步骤三：移除Excel中的乱码字符并保存为新的Excel文件
#     cleaned_df = remove_garbled_characters(xlsx_file)
#     # 将处理后的数据保存回Excel文件
#     cleaned_df.to_excel(xlsx_file, index=False)
import pandas as pd

# 读取 CSV 文件
csv_file_path = 'C:/Users/12602/radioactive_wastewater.csv'  # 替换为实际的 CSV 文件路径
df = pd.read_csv(csv_file_path)
# df = df.astype(str)
# df.replace("nan", "", inplace=True)
# df["text"] = df["text"].str.replace("http[s]?://[^\s]*", "", regex=True)  # 去掉URL
# # df["text"] = df["text"].str.replace("\n", " ", regex=True)  # 去掉换行符（使用原始字符串）
# df["text"] = df["text"].str.replace("@[^ ]*", "@Users", regex=True)  # 替换@后面的字符串为"Users"
# df = df[df["text"].str.contains("Tibet|Uyghur|tibet|uyghur")]
# for column in df.columns:
#     df[column] = df[column].apply(lambda x: x.encode('latin-1').decode('latin-1', 'ignore'))
# df = df.astype(str)
# contains_special_characters = df.apply(lambda row: any("ð" in cell or "æ" in cell or "Ø" in cell or "âï" in cell or "Â" in cell or "å" in cell or "â" in cell or "¤" in cell or "Ã" in cell or "Ä" in cell or "à" in cell or "å" in cell or "ä" in cell or "è" in cell or "ë" in cell or "Ð" in cell or "Ñ" in cell for cell in row ), axis=1)
# df = df[~contains_special_characters]
# 删除 'text' 列中的重复项
df_unique_text = df.drop_duplicates(subset=['text'])

# 将处理后的数据保存到新的 CSV 文件
output_csv_file = 'unique_text_data.csv'
df_unique_text.to_csv(output_csv_file, index=False)

print(f"处理后的数据已保存到 {output_csv_file}")
