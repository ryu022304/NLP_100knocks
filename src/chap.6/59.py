# Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての
# 名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
import sys, io, os, re
import pprint
from nltk.stem.porter import PorterStemmer
import json
import corenlp
from pycorenlp import StanfordCoreNLP
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

nlp = StanfordCoreNLP("http://localhost:9000")
prop = {"annotators":"tokenize, parse", "outputFormat":"json"}

tokenized_list = []

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        tokenized_list.append(nlp.annotate(line, properties=prop))

#pprint.pprint(tokenized_list)

for line in tokenized_list:
    sentences = line['sentences']
    if len(sentences) == 0:
        pass
    else:
        for sentence in sentences:
            print(sentence['parse'])
            root = sentence['parse'].split('ROOT')[1]
            text = root.replace('\n','').strip()
            pattern = re.compile(r'^\((.*?)\s(.*)$')
            print(text)
            res = pattern.findall(text)
            print('----------------------------')
            print(res)
