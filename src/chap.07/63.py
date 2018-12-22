# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを
# 検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，
# アーティスト名からタグと被タグ数を検索せよ．
import sys, io, os, re
import pprint
import redis
import gzip, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

r = redis.StrictRedis(host='localhost', port=6379, db=0)

'''
with gzip.open(ipath+"artist.json.gz", "rt", "utf_8") as f:
    for line in f:
        obj = json.loads(line)

        if 'tags' in obj:
            name = obj['name']
            tags = obj['tags']
            r.set(name, tags)
'''
tags = r.get('Oasis')
pprint.pprint(tags.decode())
