# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
# 素性としては，レビューからストップワードを除去し，各単語をステミング処理した
# ものが最低限のベースラインとなるであろう．

import pprint
import collections
from nltk.stem.porter import PorterStemmer as PS

ipath = '../../data/input/'
opath = '../../data/output/'

# 毎回ファイル開くとかなり時間がかかるからファイルのopenは関数の外に出した
'''
stopwords = []
with open(ipath+'stop-word-list.txt', encoding='utf-8') as f:
    stopwords = [line for line in f]
'''
# ファイルエンコードの関係かストップワードが一致しないので書き出した
stopwords = 'a,about,above,across,after,afterwards,again,against,all,almost,alone,along,already,also,although,always,am,among,amongst,amoungst,amount,an,and,another,any,anyhow,anyone,anything,anyway,anywhere,are,around,as,at,back,be,became,because,become,becomes,becoming,been,before,beforehand,behind,being,below,beside,besides,between,beyond,bill,both,bottom,but,by,call,can,cannot,cant,co,computer,con,could,couldnt,cry,de,describe,detail,do,done,down,due,during,each,eg,eight,either,eleven,else,elsewhere,empty,enough,etc,even,ever,every,everyone,everything,everywhere,except,few,fifteen,fify,fill,find,fire,first,five,for,former,formerly,forty,found,four,from,front,full,further,get,give,go,had,has,hasnt,have,he,hence,her,here,hereafter,hereby,herein,hereupon,hers,herse",him,himse",his,how,however,hundred,i,ie,if,in,inc,indeed,interest,into,is,it,its,itse",keep,last,latter,latterly,least,less,ltd,made,many,may,me,meanwhile,might,mill,mine,more,moreover,most,mostly,move,much,must,my,myse",name,namely,neither,never,nevertheless,next,nine,no,nobody,none,noone,nor,not,nothing,now,nowhere,of,off,often,on,once,one,only,onto,or,other,others,otherwise,our,ours,ourselves,out,over,own,part,per,perhaps,please,put,rather,re,same,see,seem,seemed,seeming,seems,serious,several,she,should,show,side,since,sincere,six,sixty,so,some,somehow,someone,something,sometime,sometimes,somewhere,still,such,system,take,ten,than,that,the,their,them,themselves,then,thence,there,thereafter,thereby,therefore,therein,thereupon,these,they,thick,thin,third,this,those,though,three,through,throughout,thru,thus,to,together,too,top,toward,towards,twelve,twenty,two,un,under,until,up,upon,us,very,via,was,we,well,were,what,whatever,when,whence,whenever,where,whereafter,whereas,whereby,wherein,whereupon,wherever,whether,which,while,whither,who,whoever,whole,whom,whose,why,will,with,within,without,would,yet,you,your,yours,yourself,yourselves'.lower().split(',')

def is_stopword(str):
    flag = False
    if str.lower() in stopwords:
        flag = True
    return flag

features = []
with open(opath+"sentiment.txt", encoding='cp1252') as f:
    ps = PS()
    for line in f:
        for word in line[3:].split():
            word = word.strip()
            if is_stopword(word):
                continue
            else:
                if len(word) > 1:
                    features.append(ps.stem(word))
c = collections.Counter(features).most_common()
pprint.pprint(c)
