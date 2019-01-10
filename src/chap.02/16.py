# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

ipath = '../../data/input/'
opath = '../../data/output/'

num = int(input())

all_lines = sum(1 for line in open(ipath+"hightemp.txt", encoding='utf-8'))
bunkatsu = int(all_lines / num)

with open(ipath+'hightemp.txt', encoding='utf-8') as f:
    lines = f.readlines()
    l = [ lines[i:i+bunkatsu] for i in range(0, all_lines, bunkatsu) ]

    for i,x in enumerate(l):
        with open(opath+'16'+str(i)+'.txt', mode='w', encoding='utf-8') as fw:
            for y in x:
                fw.write(y)

"""
確認コマンドと結果
$ split -l 3 ../../data/input/hightemp.txt
"""
