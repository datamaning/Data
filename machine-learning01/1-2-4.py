import numpy as np

myZero=np.zeros([3,5])
print myZero
myOnes=np.ones([3,5])
print myOnes
myRand=np.random.rand(3,4)
print myRand

myEye=np.eye(3)
print myEye
mymatrix=np.mat([[1,2,3],[4,5,6],[7,8,9]])
print 10*mymatrix
print np.sum(mymatrix)
mymatrix1=np.mat([[1,2,3],[4,5,6],[7,8,9]])
mymatrix2=1.5*np.ones(3)
print np.multiply(mymatrix1,mymatrix2)
mylist=np.mat([[1,2,3],[4,5,6],[7,8,9]])
print np.power(mylist,2)
mymatrix3=np.mat([[1],[2],[3]])
print mymatrix1*mymatrix3

print mymatrix1.T
print mymatrix1.transpose()

