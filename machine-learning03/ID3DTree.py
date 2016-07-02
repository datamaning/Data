* -*- coding: utf-8 -*-
from numpy import *
import math
import copy
import cPickle as pickle
class ID3DTree(object):
def __init__(self):
        self.tree=()
        sele.dataSet=[]
        self.labels=[]
def loadDataSet(self,path,labels):
        recordlist=[]
        fp=open(path,'rb')
        content=fp.read()
        fp.close()
        rowlist=content.splitlines()
        recordlist=[row.split("\t") for row in rowlist if row.strip()] 
        self.dataSet=recordlist
        self.labels=labels
def train(self):
        labels=copy.deepcopy(self.labels)
        self.tree=self.buildTree(self.dataSet,labels)
def buildTree(self,dataSet,labels):
    cateList=[data[-1] for data in dataSet]
#程序终止条件1:如果classList只有一种决策标签，停止划分，返回这个标签
    if cateList.count(cateList[0]==len(cateList)):
        return cateList[0]
    if len(dataSet[0])==1:
        return self.maxCate(cateList)
def maxCate(self,cateList):
    items=dict([(cateList.count(i),i) for i in cateList])
    return items[max(items.keys())]
def getBestFeat(self,dataSet):
#计算特征向量堆，其中最后一列用于类别标签，因此要减去

        
        

