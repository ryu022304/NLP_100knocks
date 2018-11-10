# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものを
# col2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
import sys, io, os
import pandas as pd
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = './data/'

data = pd.read_csv(path+"hightemp.txt", header=None, delim_whitespace=True)

data[0].to_csv(path+"col1.txt",index=False, encoding="utf-8")
data[1].to_csv(path+"col2.txt",index=False, encoding="utf-8")

cmd = "cut -f 1 " + path + "hightemp.txt > " + path + "col1-2.txt"
cmd2 = "cut -f 2 " + path + "hightemp.txt > " + path + "col2-2.txt"
subprocess.check_output(cmd, shell=True)
subprocess.check_output(cmd2, shell=True)

subprocess.check_output("diff ./data/col1.txt ./data/col1-2.txt",
 shell=True)
subprocess.check_output("diff ./data/col2.txt ./data/col2-2.txt",
 shell=True)
