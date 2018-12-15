# 84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
import sys, io, os, re
import random
import pprint
import collections
import math
import numpy as np
import pickle
from scipy import sparse, io
import sklearn.decomposition

ipath = '../../data/input/'
opath = '../../data/output/'

clf = sklearn.decomposition.TruncatedSVD(300)
Xtc = io.loadmat(opath+'84.mat')['Xtc']
Xtc_300 = clf.fit_transform(Xtc)

io.savemat(opath+'85.mat', {'Xtc_300': Xtc_300})
