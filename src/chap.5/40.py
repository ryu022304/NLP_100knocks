# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
# その結果をneko.txt.cabochaというファイルに保存せよ．
# このファイルを用いて，以下の問に対応するプログラムを実装せよ．

# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），
# 基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
# さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
# 各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
import sys, io, os, re
import CaboCha
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

'''
c = CaboCha.Parser()

list_cabocha = []
with open(ipath+'neko.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        list_cabocha.append(c.parse(line).toString(CaboCha.FORMAT_LATTICE))

with open(opath+'neko.txt.cabocha', mode='w', encoding='utf-8') as of:
    of.writelines(list_cabocha)
'''
class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface:{} base:{} pos:{} pos1:{}'.format(self.surface, self.base, self.pos, self.pos1)

def makeMorph():
    with open(opath+'neko.txt.cabocha',encoding='utf-8') as f:
        list_sentence = []
        list_morph = []
        for line in f:
            if line.split()[0] == '*':
                continue
            elif line == 'EOS\n':
                list_sentence.append(list_morph)
                list_morph = []
                continue
            else:
                word = line.split('\t')[0]
                morphs = line.split('\t')[1].split(',')
                morph = Morph(word,morphs[6],morphs[0],morphs[1])
                list_morph.append(morph)
    return list_sentence

morphed_sentences = makeMorph()

for m in morphed_sentences[2]:
    print(m)
