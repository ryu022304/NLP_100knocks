# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
# ただし，文の終端では空行を出力せよ．
import sys, io, os, re
import pprint
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

def getSentence():
    lines = []
    with open(ipath+'nlp.txt',encoding='utf-8') as f:
        for line in f:
            lines.extend(re.split('[¥.¥?!;]', line.strip()))
    return lines

def getWord(lines):
    l_list = []
    for l in lines:
        if len(l) > 1:
            l_list.extend(l.split())
            l_list.extend('\n')
    return l_list

lines = getSentence()
words = getWord(lines)

for w in words:
    print(w)
