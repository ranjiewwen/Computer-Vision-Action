# coding: utf-8

import svmMLiA

dataArr,labelArr=svmMLiA.loadDataSet('testSet.txt')
#print labelArr

# b,alphas=svmMLiA.smoSimple(dataArr,labelArr,0.6,0.001,40)
#
# print b,alphas[alphas>0]
#
# for i in range(100):
#     if alphas[i]>0.0:
#         print dataArr[i],labelArr[i]


b,alphas=svmMLiA.smoP(dataArr,labelArr,0.6,0.001,40)

print b,alphas[alphas>0]

for i in range(100):
    if alphas[i]>0.0:
        print dataArr[i],labelArr[i]