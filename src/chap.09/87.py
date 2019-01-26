# 85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
# ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
import pickle
from scipy import io
from scipy.spatial.distance import cosine

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'84.txt', 'rb') as f:
    index_ta = pickle.load(f)

Xtc_300 = io.loadmat(opath+'85.mat')['Xtc_300']

matrix_unitedstates = Xtc_300[index_ta['United_States']]
matrix_us = Xtc_300[index_ta['U.S']]

sim = 1 - cosine(matrix_unitedstates, matrix_us)

print(sim)
