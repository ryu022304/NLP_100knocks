# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ．
import sys, io, os
import subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = '../../data/input/hightemp.txt'

subprocess.check_output('expand -t 1 '+path+' > ../../data/output/11.txt', shell=True)

text = ""
text2 = ""
with open(path, encoding='utf-8') as f:
    for line in f:
        text += line.expandtabs(1)
with open('../../data/output/11.txt', encoding='utf-8') as f:
    for line in f:
        text2 += line.expandtabs(1)

#print(text)
#print(text2)

if text == text2:
    print('OK')
