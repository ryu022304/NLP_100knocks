# 記事から参照されているメディアファイルをすべて抜き出せ．
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

file_list = []
for line in text.split('\n'):
    if 'File' in line:
        start = line.index(':')
        end = line.index('|')
        file_list.append(line[start+1:end])

pprint.pprint(file_list)
