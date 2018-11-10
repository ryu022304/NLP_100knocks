# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
import sys, io, os
import subprocess
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

df = pd.read_csv(ipath+"hightemp.txt", header=None, delim_whitespace=True)
df.sort_values(by=2, ascending=False)

df.to_csv(opath+"18.txt", index=False, encoding="utf-8", header=False, sep='\t')

cmd = "sort -r -k 3 -t '\t' "+ipath+"hightemp.txt > "+opath+"18-2.txt"
subprocess.check_output(cmd, shell=True)
