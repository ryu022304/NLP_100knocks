# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
import sys, io, os, re
import pprint
import redis
import gzip, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

r = redis.StrictRedis(host='localhost', port=6379, db=0)

count = 0
keys = r.keys('*')
for key in keys:
    area = r.get(key).decode()
    #print(area)
    if area == 'Japan':
        count += 1
print(count)
