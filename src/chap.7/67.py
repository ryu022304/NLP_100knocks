# 特定の（指定した）別名を持つアーティストを検索せよ．
import sys, io, os, re
import pprint
import gzip, json
from pymongo import MongoClient
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_collection']

print("検索したい別名を入力：")
name = input()

for data in collection.find({"aliases.name": name}):
    pprint.pprint(data)
