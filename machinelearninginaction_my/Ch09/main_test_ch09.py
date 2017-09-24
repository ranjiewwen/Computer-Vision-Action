# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:11:42 2017

@author: Administrator
"""

import regTrees
from numpy import *

testMat=mat(eye(4))
print testMat
mat0,mat1=regTrees.binSplitDataSet(testMat,1,0.5)
print mat0,mat1

myDat=regTrees.loadDataSet('ex00.txt')
myMat=mat(myDat)
tree_dict=regTrees.createTree(myMat)
print tree_dict

print ' '
myDat1=regTrees.loadDataSet('ex0.txt')
myMat1=mat(myDat1)
tree_dict=regTrees.createTree(myMat1)
print tree_dict

print ' '
myDat2=regTrees.loadDataSet('ex2.txt')
myMat2=mat(myDat2)
#tree_dict=regTrees.createTree(myMat2)
print tree_dict

myTree=regTrees.createTree(myMat2,ops=(0,1))
myDataTest=regTrees.loadDataSet('ex2test.txt')
myMatTest=mat(myDataTest)
regTrees.prune(myTree,myMatTest)

## mode tree

myMat3=mat(regTrees.loadDataSet('exp2.txt'))

modelTree=regTrees.createTree(myMat3,regTrees.modelLeaf,regTrees.modelErr,(1,10))
print modelTree




