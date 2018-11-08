# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = [x.strip('.,') for x in str.split()]
word_len = [len(x) for x in words]
print(words)
print(word_len)
