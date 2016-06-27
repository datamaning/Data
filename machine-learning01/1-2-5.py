from numpy import *
A=mat([[1,2,4,5,7],[9,12,11,8,2],[6,4,3,2,1],[9,1,3,4,5],[0,2,3,4,5]])
print linalg.det(A)

print linalg.inv(A)

AT=A.T
print A*AT

print linalg.matrix_rank(A)

b=mat([[1,0,1,0,1]])
print linalg.solve(A,b.T)
A=[8,1,6]
modA=sum(power(A,2))
print modA
print sqrt(modA)
print linalg.norm(A)


