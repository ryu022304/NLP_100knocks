# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
# ただし，構文木上のパスは以下の仕様を満たすものとする．
# ・各文節は（表層形の）形態素列で表現する
# ・パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
# 「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
# 次のような出力が得られるはずである．
import pprint
import CaboCha
import pydot
import pydotplus

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
root_path_list = []
for c in chunks:
    for m in c:
        out = ''
        if m.hasNoun():
            out += m.joinMorph()
            d = m.dst
            while True:
                if d == -1:
                    break
                else:
                    out += ' -> '+c[d].joinMorph()
                    d = c[d].dst
            root_path_list.append(out)

pprint.pprint(root_path_list)
