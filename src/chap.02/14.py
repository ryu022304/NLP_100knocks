# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

ipath = '../../data/input/'
opath = '../../data/output/'

num = input()

text =''
with open(ipath+'hightemp.txt', encoding='utf-8') as fi, \
    open(opath+'14.txt', mode='w', encoding='utf-8') as fo:
    for i,line in enumerate(fi, 1):
        text += line
        if i == int(num):
            break
    fo.write(text)

"""
確認コマンドと結果
$ head -n 3 ../../data/input/hightemp.txt | diff - ../../data/output/14.txt
何も出力されない
"""
