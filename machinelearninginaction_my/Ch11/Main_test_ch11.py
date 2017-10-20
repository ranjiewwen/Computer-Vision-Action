# coding :utf-8

import apriori
# 发现频繁项集和发现关联规则

dataSet=apriori.loadDataSet()
print(dataSet)

C1=apriori.createC1(dataSet)
print (C1)

D=map(set,dataSet)
print (D)

L1,suppData0=apriori.scanD(D,C1,0.5)
print (L1)

L,suppData=apriori.apriori(dataSet)
print(L)