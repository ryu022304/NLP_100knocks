# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．
ipath = '../../data/input/'
opath = '../../data/output/'

num = int(input())

text = ""
with open(ipath+'hightemp.txt', encoding='utf-8') as fi, \
    open(opath+'15.txt', mode='w', encoding='utf-8') as fo:
    lines = fi.readlines()
    for i,line in enumerate(lines[-num:], 1):
        text += line
        if i == int(num):
            break
    fo.write(text)

"""
確認コマンドと結果
$ tail -3 ../../data/input/hightemp.txt | diff - ../../data/output/15.txt
何も出力されない
"""
