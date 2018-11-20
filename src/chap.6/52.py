# 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
# 単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの
# 実装としてstemmingモジュールを利用するとよい．
import sys, io, os, re
import pprint
from nltk.stem.porter import PorterStemmer
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

def getStemming(words):
    st = PorterStemmer()
    list_stem = []
    for w in words:
        list_stem.append('{}\t{}'.format(w, st.stem(w)))
    return list_stem

lines = getSentence()
words = getWord(lines)
stem = getStemming(words)

for s in stem:
    print(s)
