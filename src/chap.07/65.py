# MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
# さらに，これと同様の処理を行うプログラムを実装せよ．

# インタラクティブシェル
'''
mongodb
use test_database
db['test_collection'].find({"name": "Queen"})
'''

# プログラム
import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_collection']

for data in collection.find({"name": "Queen"}):
    pprint.pprint(data)
