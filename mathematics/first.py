import numpy as np
from numpy import linalg as la

a = np.array([3,-4,5])
b = np.array([1,1,-2])
print(a+b)

u=np.array([2,-7,1])
print(3*u)

v=([[1,2,1],
   [2,6,7],
   [1,5,8]])
print(np.array(v))
print(la.det(v))