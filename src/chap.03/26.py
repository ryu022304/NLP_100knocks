# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
# （弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
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
            info_dict[key] = info_dict[key]+re.sub('\'{2,5}','',line).strip()
        elif line[0] == '|':
            middle = line.index('=')
            key = line[1:middle].strip()
            info_dict[key] = re.sub('\'{2,5}','',line[middle+1:]).strip()
        elif line[0] != ('|' or '*'):
            flag_info = False
    if '基礎情報' in line:
        flag_info = True
pprint.pprint(info_dict)
