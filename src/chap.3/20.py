# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．
import sys, io, os
import gzip, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

with gzip.open(ipath+"jawiki-country.json.gz", "rt", "utf_8") as f:
    count = 0
    for line in f:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            print(obj['text'])
