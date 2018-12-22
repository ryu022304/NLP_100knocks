# 83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．
# ・f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{log(N×f(t,c)/f(t,∗)×f(∗,c)),0}
# ・f(t,c)<10ならば，Xtc=0
# ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と
# 呼ばれる統計量である．なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての
# 要素を主記憶上に載せることは無理なので注意すること．
# 幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
import sys, io, os, re
import random
import pprint
import collections
import math
import numpy as np
import pickle
from scipy import sparse, io

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'83_tc.txt', encoding='utf-8') as ftc,open(opath+'83_ta.txt', encoding='utf-8') as fta,open(opath+'83_ac.txt', encoding='utf-8') as fac,open(opath+'83_fn.txt', encoding='utf-8') as fn:

    lines_ta = fta.readlines()
    dic_ta = {}
    index_ta = collections.OrderedDict()
    for i,line in enumerate(lines_ta):
        word = line.strip('\n').split('\t')[0]
        num = int(line.strip('\n').split('\t')[1])
        dic_ta[word] = int(num)
        index_ta[word] = i

    lines_ac = fac.readlines()
    dic_ac = {}
    index_ac = collections.OrderedDict()
    for j,line in enumerate(lines_ac):
        word = line.strip('\n').split('\t')[0]
        num = int(line.strip('\n').split('\t')[1])
        dic_ac[word] = int(num)
        index_ac[word] = j

    #Xtc = np.zeros((len(dic_ta),len(dic_ac)))
    Xtc = sparse.lil_matrix((len(dic_ta), len(dic_ac)))
    N = int(fn.readline())

    lines = ftc.readlines()
    for i,line in enumerate(lines,1):
        words = line.strip('\n').split('\t')
        word_t = words[0]
        word_c = words[1]
        num_tc = int(words[2])

        if num_tc >= 10:
            PPMI = max(math.log(N*num_tc / (dic_ta[word_t]* dic_ac[word_c])), 0)
            Xtc[index_ta[word_t],index_ac[word_c]] = PPMI

    io.savemat(opath+'84.mat', {'Xtc': Xtc})
    with open(opath+'84.txt', 'wb') as f:
        pickle.dump(index_ta, f)
