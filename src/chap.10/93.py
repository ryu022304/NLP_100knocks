# 92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
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

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'91.txt',encoding='utf-8') as f,open(opath+'92_90.txt',encoding='utf-8') as fo_90, open(opath+'92_85.txt',encoding='utf-8') as fo_85:
    list_answear = []
    lines = f.readlines()
    for line in lines:
        words = line.split()
        list_answear.append(words[3])

    list_91 = []
    lines_91 = fo_90.readlines()
    for line in lines_91:
        words = line.split()
        list_91.append(words[6])

    list_85 = []
    lines_85 = fo_85.readlines()
    for line in lines_85:
        words = line.split()
        list_85.append(words[6])

    ans_90 = [ans for i,ans in enumerate(list_91) if list_answear[i]==ans]
    ans_85 = [ans for i,ans in enumerate(list_85) if list_answear[i]==ans]

    print('85:{} ({}/{})'.format(len(ans_85)/len(list_answear),len(ans_85),len(list_answear)))
    print('90:{} ({}/{})'.format(len(ans_90)/len(list_answear),len(ans_90),len(list_answear)))
