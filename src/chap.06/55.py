# 入力文中の人名をすべて抜き出せ．
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
prop = {"annotators":"tokenize, pos, lemma, ner", "outputFormat":"json"}

tokenized_list = []

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    for line in f:
        tokenized_list.append(nlp.annotate(line, properties=prop))

for line in tokenized_list:
    sentences = line['sentences']
    if len(sentences) == 0:
        pass
    else:
        for sentence in sentences:
            for token in sentence['entitymentions']:
                ner = token['ner']
                if ner == 'PERSON':
                    print(token['text'])
#pprint.pprint(tokenized_list)
