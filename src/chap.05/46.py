# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）を
# タブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．
# ・項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# ・述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
# 「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
#  この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
# 「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
import sys, io, os, re
import pprint
import CaboCha
import pydot
import pydotplus
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface:{} base:{} pos:{} pos1:{}'.format(self.surface, self.base, self.pos, self.pos1)

class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = []
        self.dst = int(dst.strip("D"))
        self.srcs = []

    def joinMorph(self):
        return ''.join([str(morph.surface) for morph in self.morphs if morph.pos != '記号'])

    def hasNoun(self):
        return any([morph.pos == '名詞' for morph in self.morphs])

    def hasVerb(self):
        return any([morph.pos == '動詞' for morph in self.morphs])


    def hasJoshi(self):
        return any([morph.pos == '助詞' or morph.pos == '格助詞' for morph in self.morphs])

    def getVerb(self):
        for morph in self.morphs:
            if morph.pos == '動詞':
                return morph.base

    def getJoshi(self):
        for morph in self.morphs:
            if morph.pos == '助詞':
                return morph.base

    def __str__(self):
        return 'surface:[{}] dst:[{}] srcs:{}'.format(' , '.join([str(morph.surface) for morph in self.morphs]), self.dst, self.srcs)

def makeChunk():
    with open(opath+'neko.txt.cabocha',encoding='utf-8') as f:
        list_chunk = []
        list_sentence = []
        chunk = None
        for line in f:
            if line.split()[0] == '*':
                if chunk is not None:
                    list_chunk.append(chunk)
                chunk = Chunk([], line.split()[2],[])
                continue
            elif line.split()[0] == 'EOS':
                if chunk is not None:
                    list_chunk.append(chunk)
                chunk = None
                list_chunk = []
                list_sentence.append(list_chunk)
                continue
            else:
                word = line.split('\t')[0]
                morphs = line.split('\t')[1].split(',')
                morph = Morph(word,morphs[6],morphs[0],morphs[1])
                chunk.morphs.append(morph)

        for chunk in list_sentence:
            for i,c in enumerate(chunk):
                src = c.dst
                if src == -1:
                    continue
                chunk[src].srcs.append(i)
    return list_sentence

chunks = makeChunk()

list_corpas = []
for c in chunks:
    for m in c:
        list_joshi = []
        list_setsu = []
        if m.hasVerb():
            verb = m.getVerb()
            for j in m.srcs:
                if c[j].hasJoshi():
                    list_joshi.append(c[j].getJoshi())
                    list_setsu.append(c[j].joinMorph())
            if len(list_joshi) > 0:
                list_joshi_s = sorted(list_joshi)
                list_corpas.append('{}\t{}\t{}\n'.format(verb, ' '.join(list_joshi_s), ' '.join(list_setsu)))
#print(list_corpas)

with open(opath+'corpas02.txt.cabocha', mode='w', encoding='utf-8') as of:
    of.writelines(list_corpas)
