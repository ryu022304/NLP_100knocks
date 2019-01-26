# 単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．
# 例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．
# ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
# https://github.com/svn2github/word2vec/blob/master/questions-words.txt

ipath = '../../data/input/'
opath = '../../data/output/'

with open(ipath+'questions-words.txt', encoding='utf-8') as fi,\
 open(opath+'91.txt', mode='a',encoding='utf-8') as fo:
    list_family = []
    lines = fi.readlines()
    flag_family = False
    for line in lines:
        if ': family' in line:
            flag_family = True
            continue
        elif ':' in line:
            flag_family = False
            pass
        if flag_family:
            list_family.append(line)
    fo.write(''.join(list_family))
