from numpy import *
v1=mat([[1,2,3,4,5]])
v2=mat([[3,4,5,6,7]]).T
cosV12=dot(v1,v2)/(linalg.norm(v1)*linalg.norm(v2))
print cosV12

