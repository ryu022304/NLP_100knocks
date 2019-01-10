# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
import pandas as pd

ipath = '../../data/input/'
opath = '../../data/output/'

df = pd.read_csv(ipath+"hightemp.txt", header=None, delim_whitespace=True)
df.sort_values(by=2, ascending=False)

df.to_csv(opath+"18.txt", index=False, encoding="utf-8", header=False, sep='\t')

"""
確認コマンドと結果
$ cat ../../data/input/hightemp.txt | sort -r -k 3 -t '\t' | diff -  ../../data/output/18.txt
"""
