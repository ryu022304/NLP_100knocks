# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものを
# col2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
import sys, io, os
import pandas as pd
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

data = pd.read_csv(ipath+"hightemp.txt", header=None, delim_whitespace=True)

data[0].to_csv(opath+"col1.txt",index=False, encoding="utf-8")
data[1].to_csv(opath+"col2.txt",index=False, encoding="utf-8")

cmd = "cut -f 1 " + ipath + "hightemp.txt > " + opath + "col1-2.txt"
cmd2 = "cut -f 2 " + ipath + "hightemp.txt > " + opath + "col2-2.txt"
subprocess.check_output(cmd, shell=True)
subprocess.check_output(cmd2, shell=True)

text = ""
text2 = ""
with open(opath+'col1.txt', encoding='utf-8') as f:
    for line in f:
        text += line
with open(opath+'col1-2.txt', encoding='utf-8') as f:
    for line in f:
        text2 += line
if text == text2:
    print('col1: OK')

text3 = ""
text4 = ""
with open(opath+'col2.txt', encoding='utf-8') as f:
    for line in f:
        text3 += line
with open(opath+'col2-2.txt', encoding='utf-8') as f:
    for line in f:
        text4 += line
if text3 == text4:
    print('col2: OK')
