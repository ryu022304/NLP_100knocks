# "Hi He Lied Because Boron Could Not Oxidize Fluorine.
# New Nations Might Also Sign Peace Security Clause. Arthur
# King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の
# 単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から
# 単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = str.split()
words_dict = {}

for i,word in enumerate(words,1):
    if i in [1,5,6,7,8,9,15,16,19]:
        words_dict[word[:1]] = i
    else:
        words_dict[word[:2]] = i

print(words_dict)
