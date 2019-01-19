# 英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，
# イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，
# 指し示している概念・実体が曖昧である．そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，
# 複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．
# インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．
# 例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
# 下記を使用した
# https://raw.githubusercontent.com/umpirsky/country-list/master/data/en_US/country.csv

ipath = '../../data/input/'
opath = '../../data/output/'

country_list = []
with open(ipath+'country.csv',encoding='utf-8') as fc:
    lines = fc.readlines()
    for line in lines[1:]:
        country_list.append(line.split(',')[1].strip('\n"'))

with open(opath+'80.txt',encoding='utf-8') as fi, open(opath+'81.txt',mode='a',encoding='utf-8') as fo:
    for line in fi:
        new_line = line
        for country in country_list:
            if country in new_line:
                new_line = new_line.replace(country,'_'.join(country.split()))
        fo.write(new_line)
