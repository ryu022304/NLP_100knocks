# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
import sys, io, os, re
import pprint
import redis
import gzip, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

r = redis.StrictRedis(host='localhost', port=6379, db=0)

area = r.get('Oasis')
print(area.decode())
