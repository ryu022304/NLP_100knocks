# Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
from nltk.stem.porter import PorterStemmer
from pycorenlp import StanfordCoreNLP

ipath = '../../data/input/'
opath = '../../data/output/'

nlp = StanfordCoreNLP("http://localhost:9000")
prop = {"annotators":"tokenize, pos, lemma", "outputFormat":"json"}

tokenized_list = []

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    for line in f:
        tokenized_list.append(nlp.annotate(line, properties=prop))

for line in tokenized_list:
    sentences = line['sentences']
    if len(sentences) == 0:
        pass
    else:
        for sentence in sentences:
            for token in sentence['tokens']:
                print('{}\t{}\t{}'.format(token['word'], token['lemma'], token['pos']))
