# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列
# 「パタトクカシーー」を得よ．
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

str = 'パトカー'
str2 = 'タクシー'
res = ''

for p,t in zip(str, str2):
    res += p + t

print(res)
