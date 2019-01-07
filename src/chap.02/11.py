# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ．

ipath = '../../data/input/'
opath = '../../data/output/'

text = ''
with open(ipath+'hightemp.txt', encoding='utf-8') as fi,\
    open(opath+'11.txt', mode='w', encoding='utf-8') as fo:
    for line in fi:
        text += line.expandtabs(1)
    fo.write(text)

"""
確認コマンドと結果
$ expand -t 1 ../../data/input/hightemp.txt | diff - ../../data/output/11.txt
何も出力されない
"""
