# 行数をカウントせよ．確認にはwcコマンドを用いよ．
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = '../../data/hightemp.txt'

with open(path) as f:
    num_lines = sum(1 for line in f)
