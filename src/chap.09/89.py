# 85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を
# 計算し，そのベクトルと類似度の高い10語とその類似度を出力せよ．
import sys, io, os, re
import random
import pprint
import collections
import math
import numpy as np
import pickle
from scipy import sparse, io
from scipy.spatial.distance import cosine
import sklearn.decomposition

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'84.txt', 'rb') as f:
    index_ta = pickle.load(f)

Xtc_300 = io.loadmat(opath+'85.mat')['Xtc_300']

matrix= Xtc_300[index_ta['Spain']] - Xtc_300[index_ta['Madrid']] + Xtc_300[index_ta['Athens']]

dic_sim = {}
for word,index in index_ta.items():
    matrix_sim = Xtc_300[index]
    dic_sim[word] = 1 - cosine(matrix, matrix_sim)

dic_sim = sorted(dic_sim.items(), key=lambda x: -x[1])

for word,sim in dic_sim[:10]:
    print('{}\t{}'.format(word,sim))
