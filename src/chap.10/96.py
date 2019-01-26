# word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
import pickle
from gensim.models import word2vec

ipath = '../../data/input/'
opath = '../../data/output/'

model_vec = word2vec.Word2Vec.load(opath+'90.txt')

country_list = []
country_name_list = []
with open(ipath+'country.csv',encoding='utf-8') as fc:
    lines = fc.readlines()
    for line in lines[1:]:
        country = line.split(',')[1].strip('\n"').replace(' ','_')

        if country in model_vec:
            country_list.append(model_vec[country])
            country_name_list.append(country)

with open(opath+'96.txt', 'wb') as f:
    pickle.dump(country_list, f)

with open(opath+'96_name.txt', 'wb') as f:
    pickle.dump(country_name_list, f)
