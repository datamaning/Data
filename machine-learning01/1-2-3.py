#!/usr/bin/env python
# encoding: utf-8

myList=[1,2,3,4,5]
length=len(myList)
a=10
for indx in xrange(length):
    myList[indx]=a*myList[indx]
print myList
import numpy as np
mymatrix=np.mat(myList)
print a*mymatrix
