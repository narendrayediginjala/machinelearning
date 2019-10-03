import pandas as pd
import quandl as qd
import math
import numpy as np
from sklearn import preprocessing,svm
from sklearn.model_selection import cross_validate,train_test_split
from sklearn.linear_model import LinearRegression

df = qd.get("WIKI/GOOG")
df.rename(columns={"Adj. Close":"adj_close","Split Ratio":"split_ratio","Adj. Open":"adj_open","Adj. High":"adj_high","Adj. Low":"adj_low","Adj. Volume":"adj_volume","Ex-Dividend":"ex_dividend"},inplace=True)
df["HL_PCT"]=(df["High"]-df["Low"])/df["High"]*100
df["OC_PCT"]=(df["Close"]-df["Open"])/df["Close"]*100
df = df[["adj_close","HL_PCT","OC_PCT","adj_volume"]]
exp_col = "adj_close"
df.fillna(-9999,inplace=True)
exp_out = int(math.ceil(0.01*len(df)))
print("exp_out value",str(exp_out))
df["label"]=df[exp_col].shift(-exp_out)
df.dropna(inplace=True)
X = np.array(df.drop(['label'],1))
print("X values")
print(X[5:])
y = np.array(df['label'])
print("y values")
print(y[5:])
X = preprocessing.scale(X)
print("Scaled values of X - ")
print(X[5:])
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
clf = LinearRegression()
clf.fit(X_train,y_train)
accuracy = clf.score(X_test,y_test)
print("Linear Regression Accuracy - ", str(accuracy))


clf2 = svm.SVR()
clf2.fit(X_train,y_train)
svm_accuracy = clf2.score(X_test,y_test)
print("SVM  Accuracy - ", str(svm_accuracy))
