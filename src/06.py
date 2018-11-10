# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，
# 'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def makeNgram(words, n):
    return [words[i:i+n] for i in range(len(words)-n+1)]

str = "paraparaparadise"
str2 = "paragraph"

X = set(makeNgram(str, 2))
Y = set(makeNgram(str2, 2))

wa = X | Y
seki = X & Y
sa = X - Y

print(X)
print(Y)

print(wa)
print(seki)
print(sa)
