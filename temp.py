# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# filename mytest1.py
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
dataSet=[[-0.017612,14.053064],[-1.395364,4.6654],[-0.752147,6.538620]
    ,[-1.322371,7.152853],[0.423363,11.054677],[0.406704,7.067335],[0.667391,2.21
    ],[-2.460150,6.688607],[0.591234,9.526312],[1.406704,2.067335],[1.667391,3.21
    ],[-4.460150,6.688607],[5.591234,9.526312],[6.406704,7.067335],[8.667391,2.21
    ],[-9.460150,6.688607],[10.591234,9.526312]]
dataMat=mat(dataSet).T
plt.scatter(dataMat[0],dataMat[1],c='red',marker='o')
X=np.linspace(-2,2,100)
Y=2.8*X+9
plt.plot(X,Y)
plt.show()