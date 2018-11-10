# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# ・英小文字ならば(219 - 文字コード)の文字に置換
# ・その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(str):
    text = ''
    for s in str:
        if s.islower():
            text += chr(219 - ord(s))
        else:
            text += s
    return text

str ="I am an NLPer"

print(cipher(str))
print(cipher(cipher(str)))
