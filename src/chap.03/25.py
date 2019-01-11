# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．
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

info_dict = {}
flag_info = False
for line in text.split('\n'):
    if flag_info:
        if line[0] == '*':
            info_dict[key] = info_dict[key]+line
        elif line[0] == '|':
            middle = line.index('=')
            key = line[1:middle]
            info_dict[key] = line[middle+1:]
        elif line[0] != ('|' or '*'):
            flag_info = False
    if '基礎情報' in line:
        flag_info = True
pprint.pprint(info_dict)
