# 特定の（指定した）別名を持つアーティストを検索せよ．
import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_collection']

name = input("検索したい別名を入力：")

for data in collection.find({"aliases.name": name}):
    pprint.pprint(data)
