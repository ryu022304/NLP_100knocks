# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．
import sys, io, os
import subprocess
import pprint
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

num = int(input())

all_lines = sum(1 for line in open(ipath+"hightemp.txt", encoding='utf-8'))
bunkatsu = int(all_lines / num)

text = ""
text2 = ""
with open(ipath+'hightemp.txt', encoding='utf-8') as f:
    lines = f.readlines()
    l = [ lines[i:i+bunkatsu] for i in range(0, all_lines, bunkatsu) ]

    for i,x in enumerate(l):
        with open(opath+'16'+str(i)+'.txt', mode='w', encoding='utf-8') as fw:
            for y in x:
                fw.write(y)

cmd = "split -" + str(bunkatsu) + " " + ipath + "hightemp.txt " + opath + "16"
subprocess.check_output(cmd, shell=True)
