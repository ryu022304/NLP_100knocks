# 84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
import numpy as np
from scipy import io
import sklearn.decomposition
from sklearn.decomposition import PCA

ipath = '../../data/input/'
opath = '../../data/output/'

Xtc = io.loadmat(opath+'84.mat')['Xtc']

# 疎行列のまま主成分分析
clf = sklearn.decomposition.TruncatedSVD(300)
Xtc_300 = clf.fit_transform(Xtc)

# 一度numpyに戻して主成分分析しようとしたらメモリ不足になった
#pca = PCA(n_components=300)
#Xtc_300 = pca.fit_transform(Xtc.toarray())

io.savemat(opath+'85.mat', {'Xtc_300': Xtc_300})
