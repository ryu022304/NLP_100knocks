# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ．
import sys, io, os
from subprocess import getoutput
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = '../../data/hightemp.txt'

text = ""
with open(path, encoding='utf-8') as f:
    for line in f:
        text += line.expandtabs(1)

command_text = getoutput('expand -t 1 '+path)

print(text)
print(command_text)

if text == command_text:
    print(OK)
