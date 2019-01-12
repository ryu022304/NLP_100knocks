# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
import MeCab
import pprint
import collections
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

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

words = [dic['surface'] for dic in list_neko]
c = collections.Counter(words).most_common()
ten_words = c[:10]

pprint.pprint(ten_words)

mpl.rcParams['font.family'] = 'AppleGothic'

list_left = []
list_height = []
for word, num in c[:10]:
    list_left.append(word)
    list_height.append(num)

left = np.array(list_left)
height = np.array(list_height)

plt.bar(range(10), height, align = "center")
plt.xticks(range(10),left)
plt.savefig(opath+'37.png')
plt.show()
