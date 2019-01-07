# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
# タブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

import pandas as pd

opath = '../../data/output/'

data1 = pd.read_csv(opath+"col1.txt")
data2 = pd.read_csv(opath+"col2.txt")

data_res = pd.concat([data1, data2], axis=1)
data_res.to_csv(opath+"col3.txt",index=False, sep='\t', encoding="utf-8")

"""
確認コマンドと結果
$ paste -d '\t' ../../data/output/col1.txt ../../data/output/col2.txt | diff - ../../data/output/col3.txt
何も出力されない
"""
