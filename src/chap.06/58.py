# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
# 「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．
# ・述語: nsubj関係とdobj関係の子（dependant）を持つ単語
# ・主語: 述語からnsubj関係にある子（dependent）
# ・目的語: 述語からdobj関係にある子（dependent）
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
prop = {"annotators":"depparse", "outputFormat":"json"}

tokenized_list = []

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        tokenized_list.append(nlp.annotate(line, properties=prop))

#pprint.pprint(tokenized_list)

deps = []
dep_list = []
dic_dep = {}
for line in tokenized_list:
    sentences = line['sentences']
    if len(sentences) == 0:
        pass
    else:
        for sentence in sentences:
            for dep in sentence['basicDependencies']:
                if dep['dep'] == 'nsubj':
                    dic_dep['jutsugo'] = dep['governorGloss']
                    dic_dep['shugo'] = dep['dependentGloss']
                if dep['dep'] == 'dobj':
                    dic_dep['jutsugo'] = dep['governorGloss']
                    dic_dep['mokutekigo'] = dep['dependentGloss']
            dep_list.append(dic_dep)
            dic_dep = {}

#pprint.pprint(dep_list)
for dep in dep_list:
    if len(dep) == 3:
        print('{}\t{}\t{}'.format(dep['shugo'],dep['jutsugo'],dep['mokutekigo']))
