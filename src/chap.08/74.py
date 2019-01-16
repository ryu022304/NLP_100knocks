# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル
# （正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．
from nltk.stem.porter import PorterStemmer as PS
from sklearn.feature_extraction.text import CountVectorizer as CV
from sklearn.linear_model import LogisticRegression

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

test_texts = [\
    'perhaps the best sports movie i''ve ever seen.', \
    'i had more fun watching spy than i had with most of the big summer movies.', \
    'vividly conveys the shadow side of the 30-year friendship between two english women.', \
    'an excruciating demonstration of the unsalvageability of a movie saddled with an amateurish screenplay.', \
    'sadly , hewitt''s forte is leaning forward while wearing low-cut gowns , not making snappy comebacks.', \
    'since lee is a sentimentalist , the film is more worshipful than your random e ! true hollywood story.'
]

with open(opath+"sentiment.txt", encoding='cp1252') as f:
    train_x = []
    train_y = []
    for line in f:
        x,y = getFeatures(line)
        train_x.append(' '.join(x))
        train_y.append(1.0 if y == '+1' else 0.0)

    cv = CV()
    #print(train_x)
    train_x_cv = cv.fit_transform(train_x)
    #print(train_x_cv)
    model = LogisticRegression()
    model.fit(train_x_cv, train_y)

    for text in test_texts:
        x = cv.transform([text])
        y = model.predict(x)
        y_p = model.predict_proba(x)
        print('元文書: '+text)
        print('予測:{}　確率:{}'.format('+1' if y[0]==1.0 else '-1', str(max(y_p[0]))))
