# The WordSimilarity-353 Test Collectionの評価データを入力とし，1列目と2列目の単語の類似度を計算し，
# 各行の末尾に類似度の値を追加するプログラムを作成せよ．
# このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
import numpy as np
from scipy.stats import spearmanr

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'94_90.txt',encoding='utf-8') as fo_90,\
    open(opath+'94_85.txt',encoding='utf-8') as fo_85:

    lines_90 = fo_90.readlines()
    list_human_90 = []
    list_sim_90 = []
    for line_90 in lines_90[1:]:
        words = line_90[:-1].split(',')
        list_human_90.append(words[2])
        list_sim_90.append(words[3])

    lines_85 = fo_85.readlines()
    list_human_85 = []
    list_sim_85 = []
    for line_85 in lines_85[1:]:
        words = line_85[:-1].split(',')
        list_human_85.append(words[2])
        list_sim_85.append(words[3])

    correlation_85,pval_85 = spearmanr(list_sim_85,list_human_85)
    correlation_90,pval_90 = spearmanr(list_sim_90,list_human_90)

    print('相関係数(85):{}'.format(correlation_85))
    print('相関係数(90):{}'.format(correlation_90))
