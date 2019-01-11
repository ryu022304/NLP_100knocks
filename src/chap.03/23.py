# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
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

section_list = []
for line in text.split('\n'):
    if '====' in line:
        section_list.append((line[4:-4].strip(),3))
    elif '===' in line:
        section_list.append((line[3:-3].strip(),2))
    elif '==' in line:
        section_list.append((line[2:-2].strip(),1))
pprint.pprint(section_list)
