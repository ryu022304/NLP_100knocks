# MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．

# インタラクティブシェル
'''
mongodb
use test-database
db['test-collection'].count({"area": "Japan"})
# db.test-collection.count()だとコレクション名にハイフンが入ってしまっているのでエラーになる
'''

# プログラム
import sys, io, os, re
import pprint
import gzip, json
from pymongo import MongoClient
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

client = MongoClient('localhost', 27017)
db = client['test-database']
collection = db['test-collection']

pprint.pprint(collection.count({"area": "Japan"}))
