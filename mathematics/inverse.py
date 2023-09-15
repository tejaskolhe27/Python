import numpy as np
from numpy import linalg as la

a= np.array([[3,5],[2,3]])
print("The inverse of matrix A is=\n", la.inv(a))
print()

b= np.array([[5,3],[2,1]])
print("The inverse of matrix B is=\n", la.inv(b))

c= np.array([[1,1,0],[1,1,1],[0,2,1]])
print("The inverse of matrix C is=\n", la.inv(c))
