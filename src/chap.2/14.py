# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．
import sys, io, os
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

num = input()

text = ""
text2 = ""
with open(ipath+'hightemp.txt', encoding='utf-8') as f:
    for i,line in enumerate(f, 1):
        text += line
        if i == int(num):
            break

cmd = "head -" + num + " " + ipath + "hightemp.txt > " + opath + "14.txt"
subprocess.check_output(cmd, shell=True)

with open(opath+'14.txt', encoding='utf-8') as f:
    for line in f:
        text2 += line
#print(text)
#print(text2)
if text == text2:
    print('OK')
