# 文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである．
# ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう．
# そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，
# 各トークンに以下の処理を施し，単語から記号を除去せよ．
# ・トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
# ・空文字列となったトークンは削除
# 以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
import bz2

ipath = '../../data/input/'
opath = '../../data/output/'

with bz2.open(ipath+'enwiki-20150112-400-r100-10576.txt.bz2', 'rt') as fi, open(opath+'80.txt',mode='a',encoding='utf-8') as fo:
    for line in fi:
        tokens = []
        if len(line) > 0:
            for word in line.split():
                tokens.append(str(word).strip('.,!?;:()[]\'"'))
        else:
            continue
        fo.write(' '.join(tokens)+'\n')
