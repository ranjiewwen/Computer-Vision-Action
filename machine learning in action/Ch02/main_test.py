# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:27:21 2017

@author: Administrator
"""

import kNN
group,labels=kNN.createDataSet()

'''
reload(kNN)
datingDataMat,datingLabels=kNN.file2matrix('datingTestSet2.txt');

reload(kNN)
normMat,ranges,minVals=kNN.autoNorm(datingDataMat)


## 测试分类器性能，可以改变k值和训练，测试集的比例；观察分类器的性能
kNN.datingClassTest()

## 单例测试
kNN.classifyPerson()

'''

## 手写体img2vector
testVector=kNN.img2vector('testDigits/0_13.txt')

kNN.handwritingClassTest()