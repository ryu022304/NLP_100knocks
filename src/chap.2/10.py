# 行数をカウントせよ．確認にはwcコマンドを用いよ．
import sys, io, os
from subprocess import getoutput
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = './data/hightemp.txt'
num_lines = 0
with open(path, encoding='utf-8') as f:
    num_lines = sum(1 for line in f)

wc = int(getoutput('wc -l ./data/hightemp.txt | awk \'{print $1}\''))

print(num_lines)
print(wc)
if num_lines == wc:
    print('OK')
