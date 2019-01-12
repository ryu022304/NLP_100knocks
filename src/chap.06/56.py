# Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を
# 代表参照表現（representative mention）に置換せよ．ただし，置換するときは，
# 「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
from nltk.stem.porter import PorterStemmer
from pycorenlp import StanfordCoreNLP

ipath = '../../data/input/'
opath = '../../data/output/'

nlp = StanfordCoreNLP("http://localhost:9000")
prop = {"annotators":"tokenize,ssplit,pos,lemma,ner,parse,dcoref", "outputFormat":"json"}

tokenized_list = []

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    for line in f:
        tokenized_list.append(nlp.annotate(line, properties=prop))

display_list = []
for line in tokenized_list:
    sentences = line['sentences']
    # sentencesがなければ改行
    if len(sentences) == 0:
        display_list.append('\n')
    else:
        core = line['corefs']
        # sentencesがあるのにcorefsがないのは参照表現がないやつ(?)
        if len(core) == 0:
            for sentence in sentences:
                for token in sentence['tokens']:
                    display_list.append(token['word'])
        # 参照表現があるやつ
        else:
            for sentence in sentences:
                for token in sentence['tokens']:
                    word = token['word']
                    index = token['index']
                    display_list.append(word)

                    for corefs in core.values():
                        for c in corefs:
                            if c['isRepresentativeMention'] == False and index == c['sentNum']:
                                display_list.append('('+c['text']+')')

print(' '.join(display_list))
