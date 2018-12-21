# word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
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
from gensim.models import word2vec
import gensim

ipath = '../../data/input/'
opath = '../../data/output/'

model_vec = word2vec.Word2Vec.load(opath+'90.txt')

country_list = []
with open(ipath+'country.csv',encoding='utf-8') as fc:
    lines = fc.readlines()
    for line in lines[1:]:
        country = line.split(',')[1].strip('\n"').replace(' ','_')

        if country in model_vec:
            country_list.append(model_vec[country])

with open(opath+'96.txt', 'wb') as f:
    pickle.dump(country_list, f)