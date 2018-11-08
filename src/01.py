# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

str = 'パタトクカシーー'

print(str[::2])
