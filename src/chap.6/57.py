# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を
# 有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，
# Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，
# pydotを使うとよい．
import sys, io, os, re
import pprint
from nltk.stem.porter import PorterStemmer
import json
import pydot_ng as pydot
import pydotplus
import corenlp
from pycorenlp import StanfordCoreNLP
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

nlp = StanfordCoreNLP("http://localhost:9000")
prop = {"annotators":"depparse", "outputFormat":"json"}

tokenized_list = []

with open(ipath+'nlp.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        tokenized_list.append(nlp.annotate(line, properties=prop))

#pprint.pprint(tokenized_list)

dots = []
edges = []
for line in tokenized_list:
    sentences = line['sentences']
    if len(sentences) == 0:
        pass
    else:
        for sentence in sentences:
            for dep in sentence['basicDependencies']:
                # ,を付けるとファイル出力時にエラーになったので省く
                if dep['dep'] != 'punct':
                    edges.append(
                    ((dep['governor'],dep['governorGloss']),
                    (dep['dependent'], dep['dependentGloss']))
                    )
            dots.append(edges)
            edges = []
#pprint.pprint(dots)

def graph_from_edges_ex(edge_list, directed=False):
    pprint.pprint(edge_list)
    if directed:
        graph = pydot.Dot(graph_type='digraph')
    else:
        graph = pydot.Dot(graph_type='graph')

    for edge in edge_list:

        id1 = str(edge[0][0])
        label1 = str(edge[0][1])
        id2 = str(edge[1][0])
        label2 = str(edge[1][1])

        # ノード追加
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # エッジ追加
        graph.add_edge(pydot.Edge(id1, id2))

    return graph

def save_graph(dot: str, file_name: str) -> None:
    g = graph_from_edges_ex(dot, directed=True)
    g.write_png(file_name, prog='dot')

for idx in range(3):
    save_graph(dots[idx], opath+'57_graph{}.jpg'.format(idx))
