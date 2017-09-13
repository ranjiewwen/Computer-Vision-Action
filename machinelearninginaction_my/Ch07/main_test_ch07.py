# coding:utf-8

import adaboost
from numpy import *

#datMat,classLabels=adaboost.loadSimpData()

# D=mat(ones((5,1))/5)
# result=adaboost.buildStump(datMat,classLabels,D)
# print result

# classifierArray=adaboost.adaBoostTrainDS(datMat,classLabels,9)
# print classifierArray
#
# reload(adaboost)
# result= adaboost.adaClassify([0,0],classifierArray)
# print result

# dataArr,labelArr=adaboost.loadDataSet('horseColicTraining2.txt')
# classifierArray=adaboost.adaBoostTrainDS(dataArr,labelArr,10)
# testArr,testLabelArr=adaboost.loadDataSet('horseColicTest2.txt')
# prediction10=adaboost.adaClassify(testArr,classifierArray)
# errArr=mat(ones((67,1)))
# errArr[prediction10!=mat(testLabelArr).T].sum()

dataArr,labelArr=adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray,aggClassEst=adaboost.adaBoostTrainDS_plt(dataArr,labelArr,10)
adaboost.plotROC(aggClassEst.T,labelArr)


