# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．
import sys, io, os
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

num = int(input())

text = ""
text2 = ""
with open(ipath+'hightemp.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for i,line in enumerate(lines[-num:], 1):
        text += line
        if i == int(num):
            break

cmd = "tail -" + str(num) + " " + ipath + "hightemp.txt > " + opath + "15.txt"
subprocess.check_output(cmd, shell=True)

with open(opath+'15.txt', encoding='utf-8') as f:
    for line in f:
        text2 += line
#print(text)
#print(text2)
if text == text2:
    print('OK')
