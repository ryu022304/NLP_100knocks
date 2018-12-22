# 85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
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

matrix_england = Xtc_300[index_ta['England']]

dic_sim = {}
for word,index in index_ta.items():
    matrix_sim = Xtc_300[index]
    dic_sim[word] = 1 - cosine(matrix_england, matrix_sim)

dic_sim = sorted(dic_sim.items(), key=lambda x: -x[1])

for word,sim in dic_sim[1:11]:
    print('{}\t{}'.format(word,sim))
