# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
import sys, io, os, re
import MeCab
import pprint
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'
dic_path = '/usr/local/lib/mecab/dic/mecab-ipadic-neologd'

m = MeCab.Tagger("-d " + dic_path)

list_neko = []
with open(opath+'neko.txt.mecab', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('EOS','\n')
        if len(line) < 3: # EOS対策
            continue
        else:
            dict_neko = dict()
            node = m.parse(line)
            feature = node.split('\t')
            word = feature[1].split(',')
            dict_neko['surface'] = feature[0]
            dict_neko['base'] = word[6]
            dict_neko['pos'] = word[0]
            dict_neko['pos1'] = word[1]

            list_neko.append(dict_neko)

noun_list = []
noun_connect_list = []
for dic in list_neko:
    if dic['pos'] == "名詞":
        noun_list.append(dic['surface'])
    else:
        if len(noun_list) > 1:
            noun_connect_list.append(''.join(noun_list))
            noun_list = []
        else:
            noun_list = []

pprint.pprint(noun_connect_list)
