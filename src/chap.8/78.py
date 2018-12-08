# 76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
# すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．
# そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
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
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

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
    X = []
    y_l = []
    for line in f:
        x,y = getFeatures(line)
        X.append(' '.join(x))
        y_l.append(1.0 if y == '+1' else 0.0)

    X_train, X_test, y_train, y_test = train_test_split(X, y_l, test_size=0.2)

    cv = CV()
    train_x_cv = cv.fit_transform(X_train)
    model = LogisticRegression()
    model.fit(train_x_cv, y_train)
    y = model.predict(cv.transform(X_test))

    print('正解率:',accuracy_score(y_test,y))
    print('適合率:',precision_score(y_test,y))
    print('再現率:',recall_score(y_test,y))
    print('f値 　:',f1_score(y_test,y))
