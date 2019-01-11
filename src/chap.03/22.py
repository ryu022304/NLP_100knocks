# 記事中でカテゴリ名を宣言している行を抽出せよ．
import gzip, json, pprint

ipath = '../../data/input/'
opath = '../../data/output/'

text = ""
with gzip.open(ipath+"jawiki-country.json.gz", "rt", "utf_8") as f:
    for line in f:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            text = obj['text']
            break

category_list = []
for line in text.split('\n'):
    if 'Category' in line:
        category_list.append(line)
        break

categoryname_list = []
for line in category_list:
    start = line.index(':')
    end = line.index(']')
    categoryname_list.append(line[start+1:end])

pprint.pprint(categoryname_list)
