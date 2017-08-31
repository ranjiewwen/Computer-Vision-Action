# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:14:37 2017

@author: Administrator
"""

'''
现有大学校园网的日志数据，290条大学生的校园网使用情况数据，数据包
括用户ID，设备的MAC地址，IP地址，开始上网时间，停止上网时间，上
网时长，校园网套餐等。 利用已有数据，分析学生上网的模式。
实验目的：
通过DBSCAN聚类，分析学生上网时间和上网时长的模式。

'''

import numpy as np
import sklearn.cluster as skc
from sklearn import metrics
import matplotlib.pyplot as plt
 
 
mac2id=dict()
onlinetimes=[]

fpath='F:\RANJIEWEN\MachineLearning\Python机器学习实战_mooc\data\聚类\\'
f=open(fpath+'TestData.txt',encoding='utf-8')
for line in f:
    mac=line.split(',')[2]
    onlinetime=int(line.split(',')[6])
    starttime=int(line.split(',')[4].split(' ')[1].split(':')[0])
    if mac not in mac2id:
        mac2id[mac]=len(onlinetimes)
        onlinetimes.append((starttime,onlinetime))
    else:
        onlinetimes[mac2id[mac]]=[(starttime,onlinetime)]
real_X=np.array(onlinetimes).reshape((-1,2))
 
X=real_X[:,0:1]
 
db=skc.DBSCAN(eps=0.01,min_samples=20).fit(X)
labels = db.labels_
 
print('Labels:')
print(labels)
raito=len(labels[labels[:] == -1]) / len(labels)
print('Noise raito:',format(raito, '.2%'))
 
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
 
print('Estimated number of clusters: %d' % n_clusters_)
print("Silhouette Coefficient: %0.3f"% metrics.silhouette_score(X, labels))
 
for i in range(n_clusters_):
    print('Cluster ',i,':')
    print(list(X[labels == i].flatten()))
     
plt.hist(X,24)