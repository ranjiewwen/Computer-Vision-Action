# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:42:55 2017

@author: Administrator
"""

# unit4 classify

#数据介绍：
#网易财经上获得的上证指数的历史数据，爬取了20年的上证指数数据。
#实验目的：
#根据给出当前时间前150天的历史数据，预测当天上证指数的涨跌。

import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import cross_validation

fpath='F:\RANJIEWEN\MachineLearning\Python机器学习实战_mooc\data\classify\stock\\000777.csv'

data=pd.read_csv(fpath,encoding='gbk',parse_dates=[0],index_col=0)
data.sort_index(0,ascending=True,inplace=True)

dayfeature=150
featurenum=5*dayfeature
x=np.zeros((data.shape[0]-dayfeature,featurenum+1))
y=np.zeros((data.shape[0]-dayfeature))

for i in range(0,data.shape[0]-dayfeature):
    x[i,0:featurenum]=np.array(data[i:i+dayfeature] \
          [[u'收盘价',u'最高价',u'最低价',u'开盘价',u'成交量']]).reshape((1,featurenum))
    x[i,featurenum]=data.ix[i+dayfeature][u'开盘价']
 
for i in range(0,data.shape[0]-dayfeature):
    if data.ix[i+dayfeature][u'收盘价']>=data.ix[i+dayfeature][u'开盘价']:
        y[i]=1
    else:
        y[i]=0          
 
clf=svm.SVC(kernel='rbf')
result = []
for i in range(5):
    x_train, x_test, y_train, y_test = \
                cross_validation.train_test_split(x, y, test_size = 0.2)
    clf.fit(x_train, y_train)
    result.append(np.mean(y_test == clf.predict(x_test)))
print("svm classifier accuacy:")
print(result)