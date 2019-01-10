# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．
import pandas as pd

ipath = '../../data/input/'
opath = '../../data/output/'

data = pd.read_csv(ipath+"hightemp.txt", header=None, delim_whitespace=True)
ken = data[0].value_counts()
ken.to_csv(opath+"19.txt", encoding="utf-8", header=False, sep='\t')

"""
確認コマンドと結果
$ cut -f 1 ../../data/input/hightemp.txt | sort | uniq -c | sort -r | awk '{print $2 " " $1}' | diff - ../../data/output/19.txt
ソートの順番は違うけどよしとする
"""
