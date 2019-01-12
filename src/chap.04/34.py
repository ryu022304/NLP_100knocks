# 2つの名詞が「の」で連結されている名詞句を抽出せよ．
import MeCab
import pprint

ipath = '../../data/input/'
opath = '../../data/output/'
dic_path = '/usr/local/lib/mecab/dic/mecab-ipadic-neologd'

m = MeCab.Tagger("-d " + dic_path)

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

noun_list = []

for i in range(1,len(list_neko)-1):
    # 「の」の前後を見て、名詞だったらリストに追加
    if list_neko[i]['base'] == "の" and list_neko[i-1]['pos'] == "名詞" and list_neko[i+1]['pos'] == "名詞":
        noun_list.append(list_neko[i-1]['base']+list_neko[i]['base']+list_neko[i+1]['base'])

pprint.pprint(noun_list)
