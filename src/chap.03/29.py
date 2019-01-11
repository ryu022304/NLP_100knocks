# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
import re
import gzip, json, pprint
import urllib.request
import urllib.parse as parse

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
            val = re.sub('\'{2,5}','',line).strip()
            val = re.sub(r'[[[]','',val)
            val = re.sub(r'[]]]','',val)
            val = re.sub(r'[*]','',val)
            info_dict[key] = info_dict[key]+val
        elif line[0] == '|':
            middle = line.index('=')
            key = line[1:middle].strip()
            val = re.sub('\'{2,5}','',line[middle+1:]).strip()
            val = re.sub(r'[[[]','',val)
            val = re.sub(r'[]]]','',val)
            val = re.sub(r'[*]','',val)
            info_dict[key] = val
        elif line[0] != ('|' or '*'):
            flag_info = False
    if '基礎情報' in line:
        flag_info = True

kokki = info_dict['国旗画像']

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'format=json&' \
    + 'action=query&' \
    + 'prop=imageinfo&' \
    + 'iiprop=url&' \
    + 'titles=File:' + parse.quote(kokki)

with urllib.request.urlopen(url) as res:
    body = json.load(res)
    
kokki_url = body['query']['pages']['-1']['imageinfo'][0]['url']
print(kokki_url)
