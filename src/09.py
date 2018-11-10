# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば"I couldn't believe that I could actually understand
# what I was reading : the phenomenal power of the human mind ."）を
# 与え，その実行結果を確認せよ．
import random

def shuffleText(text):
    words = text.split()
    ret = []
    for word in words:
        if len(word) > 4:
            random_text = list(word[1:-1])
            random.shuffle(random_text)
            ret.append(word[0]+''.join(random_text)+word[-1])
        else:
            ret.append(word)
    return ' '.join(ret)

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(shuffleText(str))
