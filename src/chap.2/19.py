# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．
import sys, io, os
import subprocess
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

data = pd.read_csv(ipath+"hightemp.txt", header=None, delim_whitespace=True)
ken = data[0].value_counts()
ken.to_csv(opath+"19.txt", encoding="utf-8", header=False, sep='\t')

cmd = "cut -f 1 "+ipath+"hightemp.txt | sort | uniq -c | sort -r | awk '{print $2 \" \" $1}' > "+opath+"19-2.txt"
subprocess.check_output(cmd, shell=True)
