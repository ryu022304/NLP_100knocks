# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def makeNgram(words, n):
    return [words[i:i+n] for i in range(len(words)-n+1)]

str ="I am an NLPer"

print(makeNgram(str.split(),2))
print(makeNgram(str,2))
