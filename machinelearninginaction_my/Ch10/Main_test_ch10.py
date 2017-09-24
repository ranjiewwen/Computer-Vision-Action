
# coding:utf-8

import kMeans

from  numpy import *

datMat=mat(kMeans.loadDataSet('testSet.txt'))
print datMat[1:5,:]


myCentroids,clustAssing=kMeans.kMeans(datMat,4)
print myCentroids
print ' '
print clustAssing