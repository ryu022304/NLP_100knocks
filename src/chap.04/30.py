# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
# その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，
# 以下の問に対応するプログラムを実装せよ．
# なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
# 品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）の
# リストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
import MeCab
import pprint

ipath = '../../data/input/'
opath = '../../data/output/'
dic_path = '/usr/local/lib/mecab/dic/mecab-ipadic-neologd'

m = MeCab.Tagger("-d " + dic_path)

'''
with open(ipath+'neko.txt', encoding='utf-8') as f:
    lines = f.readlines()
    with open(opath+'neko.txt.mecab', mode='w', encoding='utf-8') as fw:
        for line in lines:
            fw.write(m.parse(line))
'''
list_neko = []
with open(opath+'neko.txt.mecab', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('EOS','\n')
        if len(line) < 3: # EOS対策
            continue
        else:
            dict_neko = dict()
            node = m.parse(line)
            feature = node.split('\t')
            word = feature[1].split(',')
            dict_neko['surface'] = feature[0]
            dict_neko['base'] = word[6]
            dict_neko['pos'] = word[0]
            dict_neko['pos1'] = word[1]

            list_neko.append(dict_neko)

pprint.pprint(list_neko)
