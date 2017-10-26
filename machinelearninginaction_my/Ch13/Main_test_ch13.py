
# coding:utf-8

import pca

dataMat=pca.loadDataSet('testSet.txt')
lowDMat,reconMat=pca.pca(dataMat,1)
print (lowDMat.shape)

