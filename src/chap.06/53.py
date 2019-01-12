# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
# また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
import pprint
from nltk.stem.porter import PorterStemmer
from pycorenlp import StanfordCoreNLP

ipath = '../../data/input/'
opath = '../../data/output/'

nlp = StanfordCoreNLP("http://localhost:9000")
prop = {"annotators":"tokenize, pos", "outputFormat":"json"}

tokenized_list = []

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    for line in f:
        tokenized_list.append(nlp.annotate(line, properties=prop))

pprint.pprint(tokenized_list)
