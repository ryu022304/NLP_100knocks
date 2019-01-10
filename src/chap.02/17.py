# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'col1.txt', encoding='utf-8') as f:
    lines = f.readlines()
    l = [line for line in lines]
    X = set(l)
    x_list = sorted(list(X))
    with open(opath+'17.txt', mode='w', encoding='utf-8') as fw:
        for x in x_list:
            fw.write(x)

"""
確認コマンドと結果
$ sort -u ../../data/output/col1.txt | uniq | diff - ../../data/output/17.txt
1a2
> 和歌山県
12d12
< 和歌山県
と出力されるが種類は変わらないので問題ない
"""
