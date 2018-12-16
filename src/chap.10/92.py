# 91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
# そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．
# このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
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

model_vec = word2vec.Word2Vec.load(opath+'90.txt')

with open(opath+'84.txt', 'rb') as f:
    index_ta = pickle.load(f)

Xtc_300 = io.loadmat(opath+'85.mat')['Xtc_300']

def sim_word2vec(posi1, posi2, nega, n=10):
    result = model_vec.most_similar(positive = [posi1, posi2], negative = [nega], topn = n)
    fo_90.write('{} - {} + {} = {} {}\n'.format(posi1,nega,posi2,result[0][0],result[0][1]))

def sim_vector(posi1, posi2, nega):
    matrix= Xtc_300[index_ta[posi1]] - Xtc_300[index_ta[nega]] + Xtc_300[index_ta[posi2]]

    dic_sim = {}
    # 確実に冗長なのでどうにかしたい
    for word,index in index_ta.items():
        matrix_sim = Xtc_300[index]
        dic_sim[word] = 1 - cosine(matrix, matrix_sim)

    dic_sim = sorted(dic_sim.items(), key=lambda x: -x[1])
    for word,sim in dic_sim[:1]:
        fo_85.write('{} - {} + {} = {} {}\n'.format(posi1,nega,posi2,word,sim))
        print('{} - {} + {} = {} {}\n'.format(posi1,nega,posi2,word,sim))

with open(opath+'91.txt',encoding='utf-8') as f,open(opath+'92_90.txt',mode='a',encoding='utf-8') as fo_90, open(opath+'92_85.txt',mode='a',encoding='utf-8') as fo_85:
    lines = f.readlines()
    for line in lines:
        words = line.split()
        try:
            #sim_word2vec(words[1],words[2],words[0])
            sim_vector(words[1],words[2],words[0])
        except KeyError:
            # 対象単語が辞書にないと計算できないので-1を返すようにした
            #fo_90.write('{} - {} + {} = {} {}\n'.format(words[1],words[0],words[2],'unknown','-1'))
            fo_85.write('{} - {} + {} = {} {}\n'.format(words[1],words[0],words[2],'unknown','-1'))
