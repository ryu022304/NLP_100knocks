# 与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，
# 係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
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

dots = []
for idx,c in enumerate(chunks):
    head = "digraph sentence{} ".format(idx)
    body_head = "{ graph [rankdir = LR]; "
    body_list = []
    for m in c:
        if m.dst == -1:
            continue
        moto_word = m.joinMorph()
        saki_word = c[m.dst].joinMorph()
        body_list.append('"{}"->"{}"; '.format(moto_word, saki_word))
    dots.append(head + body_head + ''.join(body_list) + '}')

def save_graph(dot: str, file_name: str) -> None:
    g = pydotplus.graph_from_dot_data(dot)
    g.write_jpeg(file_name, prog='dot')

for idx in range(3):
    save_graph(dots[idx], opath+'44_graph{}.jpg'.format(idx))
