# 81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．
# ・ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
# ・単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
import random

ipath = '../../data/input/'
opath = '../../data/output/'

with open(opath+'81.txt', encoding='utf-8') as fi, open(opath+'82.txt',mode='a',encoding='utf-8') as fw:
    for line in fi:
        words = line.split()
        for i,word in enumerate(words):
            d = random.randint(1,5)
            t = word

            for j in range(max(i - d, 0), min(i + d + 1, len(words))):
                if i != j:
                    fw.write('{}\t{}\n'.format(t, words[j]))
