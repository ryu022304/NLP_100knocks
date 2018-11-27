# アーティスト情報（artist.json.gz）をデータベースに登録せよ．さらに，
# 次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
import sys, io, os, re
import pprint
import gzip, json
from pymongo import MongoClient
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

client = MongoClient('localhost', 27017)
db = client['test-database']
collection = db['test-collection']

'''
with gzip.open(ipath+"artist.json.gz", "rt", "utf_8") as f:
    for line in f:
        obj = json.loads(line)
        collection.insert_one(obj)
'''
collection.create_index('name')
collection.create_index('aliases.name')
collection.create_index('tags.value')
collection.create_index('rating.value')
