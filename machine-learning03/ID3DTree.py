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

        

