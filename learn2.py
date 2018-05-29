from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
allurls = 'datos2.csv'
allurlscsv = pd.read_csv(allurls,',',error_bad_lines=False)
allurlsdata = pd.DataFrame(allurlscsv)

allurlsdata = np.array(allurlsdata)
print allurlsdata

random.shuffle(allurlsdata)

y = [d[1] for d in allurlsdata]
corpus = [d[0] for d in allurlsdata]
vectorizer = TfidfVectorizer()
#vectorizer = TfidfVectorizer(tokenizer=getTokens)
X = vectorizer.fit_transform(corpus)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#lgs = LogisticRegression()
#lgs.fit(X_train, y_train)
#print "LR:"
#print(lgs.score(X_test, y_test))
#nn = clf = MLPClassifier(activation='tanh',learning_rate_init=0.0001,solver='sgd', alpha=1e-5,
#                    hidden_layer_sizes=(10,10,10,2), random_state=1, verbose=True)
nn = clf = MLPClassifier(activation='relu',learning_rate_init=0.01,solver='sgd', alpha=1e-5,
                    hidden_layer_sizes=(100,100,50,50), random_state=1, verbose=True)
clf.fit(X_train, y_train)
print "NN:"
print(clf.score(X_test, y_test))
query=["http://82.223.45.6/index.php?id=' or '1'='1","http://82.223.45.6/index.php?id=sdfkljsd"]
queryX=vectorizer.fit_transform(query)
print nn.predict(queryX)
