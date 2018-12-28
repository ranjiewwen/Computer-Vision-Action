# coding: utf-8

import svmMLiA
from  numpy import *
dataArr,labelArr=svmMLiA.loadDataSet('testSet.txt')
#print labelArr

# b,alphas=svmMLiA.smoSimple(dataArr,labelArr,0.6,0.001,40)
#
# print b,alphas[alphas>0]
#
# for i in range(100):
#     if alphas[i]>0.0:
#         print dataArr[i],labelArr[i]


# 完整版platt smo实现
# b,alphas=svmMLiA.smoP(dataArr,labelArr,0.6,0.001,40)
#
# print b,alphas[alphas>0]
# for i in range(100):
#     if alphas[i]>0.0:
#         print dataArr[i],labelArr[i]
#
# ws=svmMLiA.calcWs(alphas,dataArr,labelArr)
# print ws
# datMat=mat(dataArr)
# predict=datMat[0]*mat(ws)+b
# print "predict result: %f" %predict
#
# reload(svmMLiA)
# svmMLiA.testRbf()

svmMLiA.testDigits(('rbf',20))