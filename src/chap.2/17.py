# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
import sys, io, os
import subprocess
import pprint
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'col1.txt', encoding='utf-8') as f:
    lines = f.readlines()
    l = [line for line in lines]
    X = set(l)
    x_list = sorted(list(X))
    with open(opath+'17.txt', mode='w', encoding='utf-8') as fw:
        for x in x_list:
            fw.write(x)

cmd = "sort -u "+opath+"col1.txt | uniq > "+opath+"17-2.txt"
subprocess.check_output(cmd, shell=True)
