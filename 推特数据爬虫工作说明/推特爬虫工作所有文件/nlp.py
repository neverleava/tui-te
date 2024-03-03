import textacy
import spacy
import textacy.extract
from nltk.corpus import stopwords
import jieba
# from py2neo import Graph, Node, Relationship
# import pandas as pd
import re
# graph = Graph('neo4j://localhost:7687', auth=("neo4j", "cmf030610"),name = 'neo4j')
with open('111.txt', 'r',encoding='utf-8') as f:
    pattern = re.compile(r'https?:\/\/[^\s]+')
    text1 = f.read()
    text = re.sub(pattern, '', text1)
# 加载英文停用词列表
english_stopwords = set(stopwords.words('english'))

# 对正文内容进行分词并统计词频
words = [word for word in jieba.cut(text) if word not in english_stopwords and word not in '  ']
nlp = spacy.load('en_core_web_sm')
nlp.max_length = 2000000000000000
doc = nlp(text)
nodes = []
rels = []
# for ent in doc.ents:
#     print(ent.text, ent.label_)
    # node = Node(ent.text, name=ent.label_)
    # nodes.append(node)
subjs = []
objs = []
verbs = []
for sent in doc.sents:
    for subj, verb, obj in textacy.extract.subject_verb_object_triples(sent):
        subjs.append(subj)
        objs.append(obj)
        verbs.append(verb)
print(verbs)
# query1 = """
# MATCH (n:Label {name: 'Name'})
# WITH n, count(n) AS cnt
# WHERE cnt > 1
# MATCH (n)-[r]-()
# DELETE r
# WITH n
# SKIP 1
# DELETE n
# """
#
# # 执行查询语句
# graph.run(query1)
# # print(subject_node)
# # print(object_node)
# # 获取所有节点
# query = "MATCH (n) RETURN n"
# result = graph.run(query)
#
# # 遍历所有节点并打印
# for row in result:
#     node = row[0]
#     print(node)
#
# for i in range(len(subjs)):
#     for j in range(len(objs[i])):
#         # print(f'{subjs[i]} --> {objs[i][j]}')
#         n1=str(subjs[i][0])
#         subject_node = Node("Subject", name=n1)
#         n2=str(objs[i][j])
#         object_node = Node("Object", name=n2)
#         rel = Relationship(subject_node, str(verbs[i]), object_node)
#         graph.create(rel)
