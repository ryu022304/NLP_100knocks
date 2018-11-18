# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
# 46のプログラムを以下の仕様を満たすように改変せよ．
# ・「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# ・述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# ・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# ・述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
# 例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，
# 以下の出力が得られるはずである．
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

    def hasSahen(self):
        return any([morph.pos1 == 'サ変接続' for morph in self.morphs])
        
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
        flag_sahen = False
        # 動詞が含まれるか
        if m.hasVerb():
            verb = m.getVerb()
            # 動詞にかかる文節の抜き出し
            for j in m.srcs:
                # 動詞にかかる文節に助詞が含まれるか
                if c[j].hasJoshi():
                    list_joshi.append(c[j].getJoshi())
                    list_setsu.append(c[j].joinMorph())
                    if c[j].hasSahen() and c[j].getJoshi() == 'を':
                        verb = c[j].joinMorph()+verb
                        list_joshi.remove(c[j].getJoshi())
                        list_setsu.remove(c[j].joinMorph())
                        flag_sahen = True
            if flag_sahen == False:
                continue
            if len(list_joshi) > 0:
                list_joshi_s = sorted(list_joshi)
                list_corpas.append('{}\t{}\t{}\n'.format(verb, ' '.join(list_joshi_s), ' '.join(list_setsu)))
#print(list_corpas)

with open(opath+'corpas03.txt.cabocha', mode='w', encoding='utf-8') as of:
    of.writelines(list_corpas)
