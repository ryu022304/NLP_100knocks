# 行数をカウントせよ．確認にはwcコマンドを用いよ．

ipath = '../../data/input/'
num_lines = 0
with open(ipath+'hightemp.txt', encoding='utf-8') as f:
    num_lines = sum(1 for line in f)

print(num_lines)

"""
確認コマンドと結果
$ wc -l ../../data/input/hightemp.txt | awk '{print $1}'
24
"""
