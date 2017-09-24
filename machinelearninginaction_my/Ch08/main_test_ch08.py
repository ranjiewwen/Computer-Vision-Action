# coding: utf-8

import regression

from  numpy import *
xArr,yArr=regression.loadDataSet('ex0.txt')
print xArr[0:2]

ws=regression.standRegres(xArr,yArr)
print ws

xMat=mat(xArr)
yMat=mat(yArr)
yHat=xMat*ws

import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])

xCopy=xMat.copy()
xCopy.sort(0)
yHat=xCopy*ws
ax.plot(xCopy[:,1],yHat)
plt.show()

yHat=xMat*ws
print corrcoef(yHat.T,yMat ) 

reload(regression)
xArr,yArr=regression.loadDataSet('abalone.txt')
# regression.stageWise(xArr,yArr,0.01,200)
# 更改步长和迭代次数
# regression.stageWise(xArr,yArr,0.001,5000)


lgX=[]
lgY=[]

regression.setDataCollect(lgX,lgY)
