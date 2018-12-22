# 学習データに対してロジスティック回帰モデルを適用し，正解のラベル，
# 予測されたラベル，予測確率をタブ区切り形式で出力せよ．
import sys, io, os, re
import random
import pprint
import collections
from nltk.stem.porter import PorterStemmer as PS
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.feature_extraction.text import TfidfTransformer as TT
from sklearn.feature_extraction.text import TfidfVectorizer as TV
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline

ipath = '../../data/input/'
opath = '../../data/output/'

# ファイルエンコードの関係かストップワードが一致しないので書き出した
stopwords = 'a,about,above,across,after,afterwards,again,against,all,almost,alone,along,already,also,although,always,am,among,amongst,amoungst,amount,an,and,another,any,anyhow,anyone,anything,anyway,anywhere,are,around,as,at,back,be,became,because,become,becomes,becoming,been,before,beforehand,behind,being,below,beside,besides,between,beyond,bill,both,bottom,but,by,call,can,cannot,cant,co,computer,con,could,couldnt,cry,de,describe,detail,do,done,down,due,during,each,eg,eight,either,eleven,else,elsewhere,empty,enough,etc,even,ever,every,everyone,everything,everywhere,except,few,fifteen,fify,fill,find,fire,first,five,for,former,formerly,forty,found,four,from,front,full,further,get,give,go,had,has,hasnt,have,he,hence,her,here,hereafter,hereby,herein,hereupon,hers,herse",him,himse",his,how,however,hundred,i,ie,if,in,inc,indeed,interest,into,is,it,its,itse",keep,last,latter,latterly,least,less,ltd,made,many,may,me,meanwhile,might,mill,mine,more,moreover,most,mostly,move,much,must,my,myse",name,namely,neither,never,nevertheless,next,nine,no,nobody,none,noone,nor,not,nothing,now,nowhere,of,off,often,on,once,one,only,onto,or,other,others,otherwise,our,ours,ourselves,out,over,own,part,per,perhaps,please,put,rather,re,same,see,seem,seemed,seeming,seems,serious,several,she,should,show,side,since,sincere,six,sixty,so,some,somehow,someone,something,sometime,sometimes,somewhere,still,such,system,take,ten,than,that,the,their,them,themselves,then,thence,there,thereafter,thereby,therefore,therein,thereupon,these,they,thick,thin,third,this,those,though,three,through,throughout,thru,thus,to,together,too,top,toward,towards,twelve,twenty,two,un,under,until,up,upon,us,very,via,was,we,well,were,what,whatever,when,whence,whenever,where,whereafter,whereas,whereby,wherein,whereupon,wherever,whether,which,while,whither,who,whoever,whole,whom,whose,why,will,with,within,without,would,yet,you,your,yours,yourself,yourselves'.lower().split(',')

def is_stopword(str):
    flag = False
    if str.lower() in stopwords:
        flag = True
    return flag

def getFeatures(line):
    ps = PS()
    features = []
    sentiment = line[:2]
    for word in line[3:].split():
        word = word.strip()
        if is_stopword(word):
            continue
        else:
            if len(word) > 1:
                features.append(ps.stem(word))
    return features, sentiment

with open(opath+"sentiment.txt", encoding='cp1252') as f:
    train_x = []
    train_y = []
    for line in f:
        x,y = getFeatures(line)
        train_x.append(' '.join(x))
        train_y.append(1.0 if y == '+1' else 0.0)

    cv = CV()
    train_x_cv = cv.fit_transform(train_x)
    model = LogisticRegression()
    model.fit(train_x_cv, train_y)

with open(opath+"sentiment.txt", encoding='cp1252') as f:
    for text in f:
        x = cv.transform([text])
        y = model.predict(x)
        y_p = model.predict_proba(x)
        print('{}\t{}\t{}'.format(text[:2],'+1' if y[0]==1.0 else '-1', str(max(y_p[0]))))
