# 96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．さらに，クラスタリング結果をデンドログラムとして可視化せよ．
import sys, io, os, re
import random
import pprint
import collections
import math
import numpy as np
import pickle
from scipy import sparse, io
from scipy.spatial.distance import cosine
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster, set_link_color_palette
import sklearn.decomposition
from gensim.models import word2vec
import gensim
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

ipath = '../../data/input/'
opath = '../../data/output/'

country_list = []
with open(opath+'96.txt', 'rb') as f:
  country_list = np.array(pickle.load(f))

with open(opath+'96_name.txt', 'rb') as f:
  country_name_list = np.array(pickle.load(f))

ward = linkage(country_list, method='ward')

plt.xlabel('Country', fontsize=15)
plt.ylabel('Distance', fontsize=15)

dendrogram(ward, labels=country_name_list)
plt.show()
