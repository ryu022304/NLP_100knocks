# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる
# 単語の種類数を棒グラフで表したもの）を描け．
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

mpl.rcParams['font.family'] = 'AppleGothic'

list_left = []
list_height = []
for word, num in c:
    list_left.append(word)
    list_height.append(num)

plt.hist(list_height, bins=50, range=(0,50))
plt.xlim(xmin=1, xmax=50)
plt.savefig(opath+'38.png')
plt.show()
