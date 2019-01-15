# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を
# 検索するためのデータベースを構築せよ．
import redis
import gzip, json

ipath = '../../data/input/'
opath = '../../data/output/'

r = redis.StrictRedis(host='localhost', port=6379, db=0)

with gzip.open(ipath+"artist.json.gz", "rt", "utf_8") as f:
    for line in f:
        obj = json.loads(line)

        if 'name' in obj and 'area' in obj:
            #pprint.pprint(obj)
            name = obj['name']
            area = obj['area']
            r.set(name, area)
