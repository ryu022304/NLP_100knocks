# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．
# 1. rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# 2. rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 3. 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
import sys, io, os, re
import random
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ipath = '../../data/input/'
opath = '../../data/output/'

lines = []

with open(ipath+"rt-polarity.neg", encoding='cp1252') as fn:
    for line in fn:
        lines.append('-1 '+line)

with open(ipath+"rt-polarity.pos", encoding='cp1252') as fp:
    for line in fp:
        lines.append('+1 '+line)

random.shuffle(lines)

with open(opath+'sentiment.txt', mode='w', encoding='cp1252') as f:
    f.writelines(lines)

with open(opath+"sentiment.txt", encoding='cp1252') as f:
    lines = f.readlines()
    pos = 0
    neg = 0
    for line in lines:
        if line[0] == '+':
            pos += 1
        elif line[0] == '-':
            neg += 1
    print('positive: '+str(pos))
    print('negative: '+str(neg))
