# 81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
# さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
from gensim.models import word2vec

ipath = '../../data/input/'
opath = '../../data/output/'

sentences = word2vec.Text8Corpus(opath+'81.txt')
model = word2vec.Word2Vec(sentences, size=300)
model.save(opath+'90.txt')
model = word2vec.Word2Vec.load(opath+'90.txt')

print('86 -----------------------------------------')
print('United_Statesのベクトル表示')
print(model.wv['United_States'])

print('87 -----------------------------------------')
print('United_StatesとU.Sの類似度')
print(model.similarity('United_States', 'U.S'))

print('88 -----------------------------------------')
print('Englandの類似度上位10個の単語')
result = model.most_similar(positive = ['England'], topn = 10)
for w,s in result:
    print('{}\t{}'.format(w,s))

print('89 -----------------------------------------')
print('Spain-Madrid+Athensの類似度上位10個')
result = model.most_similar(positive = ['Spain','Athens'], negative = ['Madrid'], topn = 10)
for w,s in result:
    print('{}\t{}'.format(w,s))
