# 英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
# 入力された文書を1行1文の形式で出力せよ．
import re

ipath = '../../data/input/'
opath = '../../data/output/'

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    lines = []
    for line in f:
        lines.extend(re.split('[¥.¥?!;]', line.strip()))
    for l in lines:
        if len(l) > 1:
            print(l)
