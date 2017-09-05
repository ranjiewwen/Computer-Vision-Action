# coding: utf-8

import bayes
from numpy import *


# listOposts,listClasses=bayes.loadDataSet()
# myVocablist=bayes.createVocabList(listOposts)
#
# print  myVocablist

# result=bayes.setOfWords2Vec(myVocablist,listOposts[0])
# print  result

# trainMat=[]
# for postinDoc in listOposts:
#     trainMat.append(bayes.setOfWords2Vec(myVocablist,postinDoc))
#
# p0V,p1V,pAb=bayes.trainNB0(trainMat,listClasses)
# print p0V,p1V,pAb

# bayes.testingNB()

# emailText=open('email/ham/6.txt').read()
# import re
# regEx=re.compile('\\W*')
# listOfTokens=regEx.split(emailText)
# print listOfTokens

# bayes.spamTest()

import feedparser
ny=feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf=feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
# vocabList,pSF,pNY=bayes.localWords(ny,sf)
bayes.getTopWords(ny,sf)