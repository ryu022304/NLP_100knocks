# 40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素
# （Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
# 係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
# さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトの
# リストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，
# ここで作ったプログラムを活用せよ．
import CaboCha

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

for i, c in enumerate(chunks[8]):
    print(i, c)
