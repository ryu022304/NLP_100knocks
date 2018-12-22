# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
# タブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
import sys, io, os
import pandas as pd
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

opath = '../../data/output/'

data1 = pd.read_csv(opath+"col1.txt")
data2 = pd.read_csv(opath+"col2.txt")

data_res = pd.concat([data1, data2], axis=1)

data_res.to_csv(opath+"col3.txt",index=False, sep='\t', encoding="utf-8")

cmd = "paste -d '\t' "+opath+"col1.txt "+opath+"col2.txt > "+opath+"col3-2.txt"
subprocess.check_output(cmd, shell=True)

text = ""
text2 = ""
with open(opath+'col3.txt', encoding='utf-8') as f:
    for line in f:
        text += line
with open(opath+'col3-2.txt', encoding='utf-8') as f:
    for line in f:
        text2 += line
if text == text2:
    print('OK')
