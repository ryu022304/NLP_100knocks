# 96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．さらに，クラスタリング結果をデンドログラムとして可視化せよ．
import numpy as np
import pickle
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster, set_link_color_palette
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
plt.savefig(opath+'98.png')
plt.show()
