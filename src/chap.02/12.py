# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものを
# col2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import pandas as pd

ipath = '../../data/input/'
opath = '../../data/output/'

data = pd.read_csv(ipath+"hightemp.txt", header=None, delim_whitespace=True)

data[0].to_csv(opath+"col1.txt",index=False, encoding="utf-8")
data[1].to_csv(opath+"col2.txt",index=False, encoding="utf-8")

"""
確認コマンドと結果
$ cut -f 1 ../../data/input/hightemp.txt | diff - ../../data/output/col1.txt
何も出力されない
$ cut -f 2 ../../data/input/hightemp.txt | diff - ../../data/output/col2.txt
何も出力されない
"""
