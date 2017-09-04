# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:33:00 2017

@author: Administrator
"""

import numpy as np

from sklearn.linear_model import Ridge
from sklearn import cross_validation
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

fpath='F:\RANJIEWEN\MachineLearning\Python机器学习实战_mooc\data\回归\岭回归.csv'

data=pd.read_csv(fpath,encoding='gbk',parse_dates=[0],index_col=0)

#data.sort_index(0,ascending=True,inplace=True)

X=data.iloc[:,:4]  ##语法
y=data.iloc[:,4] 
poly=PolynomialFeatures(6) #设置多项式的最高次数
X=poly.fit_transform(X)

train_set_X,test_set_X,train_set_y,test_set_y=   \
    cross_validation.train_test_split(X,y,test_size=0.3,random_state=0) #设置测试集的比例，random_state随机数种子

clf=Ridge(alpha=1.0,fit_intercept=True)
clf.fit(train_set_X,train_set_y)
clf.score(test_set_X,test_set_y)  


#plot
start=200
end=300
y_pre=clf.predict(X)
time=np.arange(start,end)
plt.plot(time,y[start:end],'b',label='real')
plt.plot(time,y_pre[start:end],'r',label='predict')
plt.legend(loc='upper left')
plt.show()