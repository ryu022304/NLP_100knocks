# 82の出力を利用し，以下の出現分布，および定数を求めよ．
# f(t,c): 単語tと文脈語cの共起回数
# f(t,∗): 単語tの出現回数
# f(∗,c): 文脈語cの出現回数
# N: 単語と文脈語のペアの総出現回数
import sys, io, os, re
import random
import pprint
import collections

ipath = '../../data/input/'
opath = '../../data/output/'

func_t_c = []
func_t_asta = []
func_asta_c = []

with open(opath+'82.txt', encoding='utf-8') as f,open(opath+'83_tc.txt',mode='a', encoding='utf-8') as ftc,open(opath+'83_ta.txt', mode='a',encoding='utf-8') as fta,open(opath+'83_ac.txt', mode='a',encoding='utf-8') as fac,open(opath+'83_fn.txt', mode='a',encoding='utf-8') as fn:
    lines = f.readlines()
    for i,line in enumerate(lines,1):
        words = line.strip('\n').split('\t')

        func_t_c.append(line.strip('\n'))
        func_t_asta.append(words[0])
        func_asta_c.append(words[1])

    count_f_t_c = collections.Counter(func_t_c)
    count_f_t_a = collections.Counter(func_t_asta)
    count_f_a_c = collections.Counter(func_asta_c)
    N = i
    fn.write(str(N))

    for k,v in count_f_t_c.most_common():
        ftc.write('{}\t{}\n'.format(k,v))
    for k,v in count_f_t_a.most_common():
        fta.write('{}\t{}\n'.format(k,v))
    for k,v in count_f_a_c.most_common():
        fac.write('{}\t{}\n'.format(k,v))
