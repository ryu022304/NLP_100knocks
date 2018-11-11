# 記事中でカテゴリ名を宣言している行を抽出せよ．
import sys, io, os
import gzip, json, pprint
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

text = ""
with gzip.open(ipath+"jawiki-country.json.gz", "rt", "utf_8") as f:
    for line in f:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            text = obj['text']

category_list = []
for line in text.split('\n'):
    if 'Category' in line:
        category_list.append(line)
pprint.pprint(category_list)
