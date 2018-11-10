# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
# タブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
import sys, io, os
import pandas as pd
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = './data/'

data1 = pd.read_csv(path+"col1.txt")
data2 = pd.read_csv(path+"col2.txt")

data_res = pd.concat([data1, data2], axis=1)

data_res.to_csv(path+"col3.txt",index=False, sep='\t', encoding="utf-8")

cmd = "paste -d '\t' ./data/col1.txt ./data/col2.txt > ./data/col3-2.txt"
subprocess.check_output(cmd, shell=True)

subprocess.check_output("diff ./data/col3.txt ./data/col3-2.txt",
 shell=True)
