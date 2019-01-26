# The WordSimilarity-353 Test Collectionの評価データを入力とし，1列目と2列目の単語の類似度を計算し，
# 各行の末尾に類似度の値を追加するプログラムを作成せよ．
# このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
import pickle
from scipy import io
from gensim.models import word2vec
import gensim

ipath = '../../data/input/'
opath = '../../data/output/'

model_vec = word2vec.Word2Vec.load(opath+'90.txt')

with open(opath+'84.txt', 'rb') as f:
    index_ta = pickle.load(f)

Xtc_300 = io.loadmat(opath+'85.mat')['Xtc_300']

def sim_word2vec(word1, word2):
    return model_vec.similarity(word1, word2)

def sim_vector(word1, word2):
    return 1 - cosine(Xtc_300[index_ta[word1]], Xtc_300[index_ta[word2]])

with open(ipath+'wordsim353/combined.csv',encoding='utf-8') as f,\
    open(opath+'94_90.txt',mode = 'a',encoding='utf-8') as fo_90,\
    open(opath+'94_85.txt',mode = 'a',encoding='utf-8') as fo_85:

    lines = f.readlines()
    for line in lines:
        words = line[:-1].split(',')
        print(words)
        try:
            sim_85 = sim_vector(words[0],words[1])
            #sim_90 = sim_word2vec(words[0],words[1])
            fo_85.write('{},{},{},{}\n'.format(words[0],words[1],words[2],str(sim_85)))
            #fo_90.write('{},{},{},{}\n'.format(words[0],words[1],words[2],str(sim_90)))
            print(line)
        except KeyError:
            fo_85.write('{},{},{},{}\n'.format(words[0],words[1],words[2],str(-1)))
            #fo_90.write('{},{},{},{}\n'.format(words[0],words[1],words[2],str(-1)))
