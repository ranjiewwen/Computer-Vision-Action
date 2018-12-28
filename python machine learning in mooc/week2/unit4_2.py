# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:41:21 2017

@author: Administrator
"""

'''
现在收集了来自 A,B,C,D,E 5位用户的可穿戴设备上的传感器数据，
每位用户的数据集包含一个特征文件（a.feature）和一个标签文件
（a.label）
特征文件中每一行对应一个时刻的所有传感器数值，标签文件中每行记录了
和特征文件中对应时刻的标记过的用户姿态，两个文件的行数相同，相同行
之间互相对应
标签文件内容如图所示，每一行代表与特征文件中对应行的用户姿态类别。
总共有0-24共25种身体姿态，如，无活动状态，坐态、跑态等。标签文件作为
训练集的标准参考准则，可以进行特征的监督学习。

假设现在出现了一个新用户，但我们只有传感器采集的数据，那么该如何得到
这个新用户的姿态呢？
或者对同一用户如果传感器采集了新的数据，怎么样根据新的数据判断当前
用户处于什么样的姿态呢？
'''

import pandas as pd
import numpy as np

from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

def load_datasets(feature_paths,label_paths):
    feature=np.ndarray(shape=(0,41))
    label=np.ndarray(shape=(0,1))
    for file in feature_paths:
        df=pd.read_table(file,delimiter=',',na_values='?',header=None)
        imp=Imputer(missing_values='NaN',strategy='mean',axis=0)
        imp.fit(df)
        df=imp.transform(df)
        feature=np.concatenate((feature,df))
        
    for file in label_paths:
        df=pd.read_table(file,header=None)
        label=np.concatenate((label,df))
    
    label=np.ravel(label)
    return feature,label
        
if __name__ == '__main__':
    ''' 数据路径 '''
    fpath='F:/RANJIEWEN/MachineLearning/Python机器学习实战_mooc/data/classify/dataset/'
    featurePaths = [fpath+'A/A.feature',fpath+'B/B.feature',fpath+'C/C.feature',fpath+'D/D.feature',fpath+'E/E.feature']
    labelPaths = [fpath+'A/A.label',fpath+'B/B.label',fpath+'C/C.label',fpath+'D/D.label',fpath+'E/E.label']
    ''' 读入数据  '''
    x_train,y_train = load_datasets(featurePaths[:4],labelPaths[:4])
    x_test,y_test = load_datasets(featurePaths[4:],labelPaths[4:])
    x_train, x_, y_train, y_ = train_test_split(x_train, y_train, test_size = 0.0)
     
    print('Start training knn')
    knn = KNeighborsClassifier().fit(x_train, y_train)
    print('Training done')
    answer_knn = knn.predict(x_test)
    print('Prediction done')
     
    print('Start training DT')
    dt = DecisionTreeClassifier().fit(x_train, y_train)
    print('Training done')
    answer_dt = dt.predict(x_test)
    print('Prediction done')
     
    print('Start training Bayes')
    gnb = GaussianNB().fit(x_train, y_train)
    print('Training done')
    answer_gnb = gnb.predict(x_test)
    print('Prediction done')
     
    print('\n\nThe classification report for knn:')
    print(classification_report(y_test, answer_knn))
    print('\n\nThe classification report for DT:')
    print(classification_report(y_test, answer_dt))
    print('\n\nThe classification report for Bayes:')
    print(classification_report(y_test, answer_gnb))