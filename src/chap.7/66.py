# MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．

# インタラクティブシェル
'''
mongodb
use test_database
db['test_collection'].count({"area": "Japan"})
'''

# プログラム
import sys, io, os, re
import pprint
import gzip, json
from pymongo import MongoClient
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_collection']

pprint.pprint(collection.count({"area": "Japan"}))
