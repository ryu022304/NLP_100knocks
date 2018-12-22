# 文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
# ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
# ・問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現
#   （表層形の形態素列）を"->"で連結して表現する
# ・文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
#また，係り受けパスの形状は，以下の2通りが考えられる．
# ・文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
#　・上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
#   文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，
#   文節kの内容を"|"で連結して表示
# 例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）
# から，次のような出力が得られるはずである．
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

    def noun_masked_surface(self, mask, dst=False):
        '''名詞を指定文字(mask)でマスクした表層形を返す
        dstがTrueの場合は最左の名詞をマスクした以降は切り捨てて返す

        戻り値：
        名詞をマスクした表層形
        '''
        result = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                if morph.pos == '名詞':
                    result += mask
                    if dst:
                        return result
                    mask = ''       # 最初に見つけた名詞をマスク、以降の名詞は除去
                else:
                    result += morph.surface
        return result

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
# 結果ファイル作成
with open(opath+'arrow.txt', mode='w', encoding='utf-8') as out_file:
    # 1文ずつリスト作成
    for chunks in chunks:

        # 名詞を含むchunkに限定した、chunksにおけるインデックスのリストを作成
        indexs_noun = [i for i in range(len(chunks)) if chunks[i].hasNoun]

        # 2つ以上ある？
        if len(indexs_noun) < 2:
            continue

        # 名詞を含むchunkの組み合わせを総当りでチェック
        for i, index_x in enumerate(indexs_noun[:-1]):
            for index_y in indexs_noun[i + 1:]:

                meet_y = False          # Yにぶつかった？
                index_dup = -1          # XとYの経路がぶつかったchunkのindex
                routes_x = set()        # Xの経路チェック用

                # 名詞Xから根に向かって、Yにぶつからないか調べながら探索
                dst = chunks[index_x].dst
                while dst != -1:
                    if dst == index_y:
                        meet_y = True           # Yにぶつかった
                        break
                    routes_x.add(dst)           # 経路チェックのために保存
                    dst = chunks[dst].dst

                # 名詞Yから根まで、Xの経路にぶつからないか調べながら探索
                if not meet_y:
                    dst = chunks[index_y].dst
                    while dst != -1:
                        if dst in routes_x:
                            index_dup = dst     # Xの経路とぶつかった
                            break
                        else:
                            dst = chunks[dst].dst

                # 結果出力
                if index_dup == -1:

                    # XからYにぶつかるパターン
                    out_file.write(chunks[index_x].noun_masked_surface('X'))
                    dst = chunks[index_x].dst
                    while dst != -1:
                        if dst == index_y:
                            out_file.write(
                                    ' -> ' + chunks[dst].noun_masked_surface('Y', True))
                            break
                        else:
                            out_file.write(
                                    ' -> ' + chunks[dst].joinMorph())
                        dst = chunks[dst].dst
                    out_file.write('\n')

                else:

                    # 経路上の共通のchunkでぶつかるパターン

                    # Xからぶつかる手前までを出力
                    out_file.write(chunks[index_x].noun_masked_surface('X'))
                    dst = chunks[index_x].dst
                    while dst != index_dup:
                        out_file.write(' -> ' + chunks[dst].joinMorph())
                        dst = chunks[dst].dst
                    out_file.write(' | ')

                    # Yからぶつかる手前までを出力
                    out_file.write(chunks[index_y].noun_masked_surface('Y'))
                    dst = chunks[index_y].dst
                    while dst != index_dup:
                        out_file.write(' -> ' + chunks[dst].joinMorph())
                        dst = chunks[dst].dst
                    out_file.write(' | ')

                    # ぶつかったchunkを出力
                    out_file.write(chunks[index_dup].joinMorph())
                    out_file.write('\n')
