# Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての
# 名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
import pprint, re
import json
from nltk.stem.porter import PorterStemmer
from pycorenlp import StanfordCoreNLP

ipath = '../../data/input/'
opath = '../../data/output/'

nlp = StanfordCoreNLP("http://localhost:9000")
prop = {"annotators":"tokenize, parse", "outputFormat":"json"}

tokenized_list = []

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        tokenized_list.append(nlp.annotate(line, properties=prop))

# 下記サイトの内容を流用
# https://qiita.com/segavvy/items/0c14bcc7f6a983554637

pattern = re.compile(r'''
    ^
    \(          # S式の開始カッコ
        (.*?)   # = タグ
        \s      # 空白
        (.*)    # = 内容
    \)          # s式の終わりのカッコ
    $
    ''', re.VERBOSE + re.DOTALL)

def ParseAndExtractNP(str, list_np):
    match = pattern.match(str.lstrip('\\n'))
    tag = match.group(1)
    value = match.group(2)

    depth = 0       # カッコの深さ
    chunk = ''      # 切り出し中の文字列
    words = []
    for c in value:
        if c == '(':
            chunk += c
            depth += 1      # 深くなった

        elif c == ')':
            chunk += c
            depth -= 1      # 浅くなった
            if depth == 0:
                words.append(ParseAndExtractNP(chunk, list_np))
                chunk = ''
        else:
            if not (depth == 0 and c == ' '):
                chunk += c

    if chunk != '':
        words.append(chunk)

    result = ' '.join(words)

    if tag == 'NP':
        list_np.append(result)

    return result

for line in tokenized_list:
    sentences = line['sentences']
    if len(sentences) == 0:
        pass
    else:
        for sentence in sentences:
            result = []
            ParseAndExtractNP(json.dumps(sentence['parse'])[1:-1], result)
            print(*result, sep='\n')
