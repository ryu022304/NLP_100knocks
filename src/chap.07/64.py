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
db = client['test_database']
collection = db['test_collection']


with gzip.open(ipath+"artist.json.gz", "rt", "utf_8") as f:
    buf = []
    for i,line in enumerate(f):
        obj = json.loads(line)
        buf.append(obj)
        if i % 10000 == 0:
            collection.insert_many(buf)
            buf = []
    collection.insert_many(buf)

collection.create_index('name')
collection.create_index('aliases.name')
collection.create_index('tags.value')
collection.create_index('rating.value')
