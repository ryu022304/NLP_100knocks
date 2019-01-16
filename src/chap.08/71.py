# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，
# 引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
# それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．

# ストップワードのリストは下記URLからダウンロードした
# http://xpo6.com/download-stop-word-list/

ipath = '../../data/input/'
opath = '../../data/output/'

def is_stopword(str):
    result = []
    flag = False
    with open(ipath+'stop-word-list.txt', encoding='utf-8') as f:
        result = [line for line in f]
    if str.lower() in result:
        flag = True
    return flag

#assert is_stopword('a')
assert is_stopword('The')
#assert is_stopword('couldnt')
#assert is_stopword('WHO')
#assert is_stopword('yourselves')

assert not is_stopword('anaconda')
assert not is_stopword('Brother')
assert not is_stopword('COOL')
assert not is_stopword('WORLD')
assert not is_stopword('Zoo')
