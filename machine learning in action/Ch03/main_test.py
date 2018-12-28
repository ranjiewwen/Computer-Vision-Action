# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 11:11:39 2017

@author: ranjiewen
"""

import trees
import treePlotter

#myDat,labels=trees.createDataSet()
# result=trees.calcShannonEnt(myDat)
# print result,myDat

### 增加更多的分类，观察熵如何变化
#myDat[0][-1]='maybe'
#result=trees.calcShannonEnt(myDat)
#print result,myDat

# reload(trees)
# trees.splitDataSet(myDat,0,0)

# reload(trees)
# result=trees.chooseBestFeatureToSplit(myDat)
# print result

# reload(trees)
# myDat,labels=trees.createDataSet()
# myTree=trees.createTree(myDat,labels)
# print myTree


# treePlotter.createPlot()

# reload(treePlotter)
# myTree= treePlotter.retrieveTree(1)
# print myTree
# treePlotter.getNumLeafs(myTree)
# treePlotter.getTreeDepth(myTree)


# reload(treePlotter)
# myTree=treePlotter.retrieveTree(0)
# treePlotter.createPlot(myTree)

# myDat,labels=trees.createDataSet()
# myTree=treePlotter.retrieveTree(0)
# # predict_result=trees.classify(myTree,labels,[1,0])
# # print predict_result
# trees.storeTree(myTree,'classifierStorage.txt')
# result=trees.grabTree('classifierStorage.txt')
# print result

fr=open('lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels=['age','prescript','astigmatic','tearRate']
lensesTree=trees.createTree(lenses,lensesLabels)
print  lensesTree
treePlotter.createPlot(lensesTree)
