# coding:utf-8

# SVD implement

from numpy import *

U,Sigma,VT=linalg.svd([[1,1],[7,7]])
#print (U,Sigma,VT)

import svdRec

Data=svdRec.loadExData()
U,Sigma,VT=linalg.svd(Data)
print (Sigma) # 返回对角线的元素节省空间
print(Sigma.shape)

Sig3=mat([[Sigma[0],0,0],[0,Sigma[1],0],[0,0,Sigma[1]]])

rec_image=U[:,:3]*Sig3*VT[:3,:]
print (rec_image)

myMat=mat(svdRec.loadExData())
dis=svdRec.ecludSim(myMat[:,0],myMat[:,4])
print (dis)

dis=svdRec.cosSim(myMat[:,0],myMat[:,4])
print dis

dis=svdRec.pearsSim(myMat[:,0],myMat[:,4])
print dis

svdRec.recommend(myMat,2)