# "dance"というタグを付与されたアーティストの中でレーティングの投票数が
# 多いアーティスト・トップ10を求めよ．
import sys, io, os, re
import pprint
import gzip, json
import pymongo
from pymongo import MongoClient
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_collection']

for data in collection.find({"tags.value": "dance"}).sort("rating.value",pymongo.DESCENDING).limit(10):
    pprint.pprint(data)
