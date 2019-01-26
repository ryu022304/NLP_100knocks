# 96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
import numpy as np
import pickle
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster, set_link_color_palette
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

ipath = '../../data/input/'
opath = '../../data/output/'

country_list = []
with open(opath+'96.txt', 'rb') as f:
  country_list = np.array(pickle.load(f))

with open(opath+'96_name.txt', 'rb') as f:
  country_name_list = np.array(pickle.load(f))

tsne = TSNE(n_components=2, random_state=0).fit_transform(country_list)
kmean = KMeans(n_clusters=5).fit_predict(country_list)

fig, ax = plt.subplots()
cmap = plt.get_cmap('Set1')
for index, label in enumerate(country_name_list):
    cval = cmap(kmean[index] / 4)
    ax.scatter(tsne[index, 0], tsne[index, 1], marker='.', color=cval)
    ax.annotate(label, xy=(tsne[index, 0], tsne[index, 1]), color=cval)

plt.savefig(opath+'99.png')
plt.show()
