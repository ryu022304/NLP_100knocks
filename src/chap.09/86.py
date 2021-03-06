# 85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
# ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
import pprint
import pickle
from scipy import io

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'84.txt', 'rb') as f:
    index_ta = pickle.load(f)

Xtc_300 = io.loadmat(opath+'85.mat')['Xtc_300']

pprint.pprint(Xtc_300[index_ta['United_States']])
pprint.pprint(Xtc_300[index_ta['United_States']].shape)
