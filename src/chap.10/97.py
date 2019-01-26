# 96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．
import numpy as np
import pickle
import pprint
from gensim.models import word2vec
from sklearn.cluster import KMeans

ipath = '../../data/input/'
opath = '../../data/output/'

model_vec = word2vec.Word2Vec.load(opath+'90.txt')

country_list = []
with open(opath+'96.txt', 'rb') as f:
  country_list = np.array(pickle.load(f))

with open(opath+'96_name.txt', 'rb') as f:
  country_name_list = np.array(pickle.load(f))

kmean_labels = KMeans(n_clusters=5, random_state=10).fit(country_list).labels_

kmean_list = []
for i,country in enumerate(country_name_list):
    kmean_list.append('{} {}'.format(kmean_labels[i],country))

pprint.pprint(sorted(kmean_list))
