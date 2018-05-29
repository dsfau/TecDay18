from sets import Set
import math
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import random
from flask import request, url_for, Flask
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import json
import re
import urlparse
num_char=re.compile('\d')
alp_char=re.compile('[A-Za-z]')
special_char=re.compile('[^a-zA-Z\d]')
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.cross_validation import train_test_split
alldata="./datos.csv"
fdata=pd.read_csv(alldata, ",", error_bad_lines=False)
loaddata=np.array(pd.DataFrame(fdata))
random.shuffle(loaddata)
print loaddata
y = [d[6] for d in loaddata]
X = [d[:-1] for d in loaddata]
X_tr, X_te, Y_tr, Y_te =  train_test_split(X, y, test_size=0.2, random_state=42)
nn = MLPClassifier(activation='relu',learning_rate_init=0.01,solver='sgd', alpha=1e-4,
                            hidden_layer_sizes=(50,100,50), random_state=42, verbose=True)
sgd = SGDClassifier()
sgd.fit(X_tr, Y_tr)
rfc = RandomForestClassifier()
rfc.fit(X_tr, Y_tr)
print "RFC:"
print(rfc.score(X_te, Y_te))
print "SGD:"
print(sgd.score(X_te, Y_te))
lgs = LogisticRegression()
lgs.fit(X_tr, Y_tr)
print "LR:"
print(lgs.score(X_te, Y_te))
nn.fit(X_tr, Y_tr)
print "NN:"
print(nn.score(X_te, Y_te))
def entropy4(st):
    stList = list(st)
    alphabet = list(Set(stList)) # list of symbols in the string
    freqList = []
    for symbol in alphabet:
        ctr = 0
        for sym in stList:
            if sym == symbol:
                ctr += 1
        freqList.append(float(ctr) / len(stList))
    ent = 0.0
    for freq in freqList:
        ent = ent + freq * math.log(freq, 2)
    ent = -ent
    return ent
app = Flask(__name__)
@app.route("/url",methods=['POST'])
def post():
    values = request.json
    params=['id','notice','username','password','email']
    url = values['url']
    predictions=[]
    for z in urlparse.urlparse(url).query.split('&'):
        parameter = z.split("=")[0]
        indice=params.index(parameter)
        query = z[len(parameter)+1:]
        print query
        ar=[indice, len(query), entropy4(query), len(num_char.findall(query)), len(alp_char.findall(query)), len(special_char.findall(query))]
        predictions.append(nn.predict(np.array(ar)))
        predictions.append(lgs.predict(np.array(ar)))
        predictions.append(sgd.predict(np.array(ar)))
        predictions.append(rfc.predict(np.array(ar)))
        print "NN:"+str(predictions[0])
        print "LGS:"+str(predictions[1])
        print "SGD:"+str(predictions[2])
        print "RFC:"+str(predictions[3])
    if "bad" in predictions:
        return "1"
    else:
        return "0"
app.run(debug=True)
