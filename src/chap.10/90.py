# 81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
# さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
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

'''
sentences = word2vec.Text8Corpus(opath+'81.txt')
model = word2vec.Word2Vec(sentences, size=300)
model.save(opath+'90.txt')
'''
model = word2vec.Word2Vec.load(opath+'90.txt')

# 入力された単語から近い単語をn個表示する
def s(posi, nega=[], n=10):
    cnt = 1 # 表示した単語の個数カウント用
    # 学習済みモデルからcos距離が最も近い単語n個(topn個)を表示する
    result = model.most_similar(positive = posi, negative = nega, topn = n)
    for r in result:
        print(cnt,' ', r[0],' ', r[1])
        cnt += 1

if __name__ == '__main__':
    #word = sys.argv[1]
    s(['Spain','Athens'],['Madrid'])
