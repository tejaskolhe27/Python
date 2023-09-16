import numpy as np
from numpy import linalg as la
import svd

a= np.array([[3,2],[2,-6]])
v1= a[0]
v2 = a[1]
u1 = v1/la.norm(v1)
w2 = v2 - np.dot(u1,v2)*u1
u2 = w2/la.norm(w2)
ona = np.array([u1,u2])
print(ona)
print("*"*100)
print(svd.ortho_2d(np.array([[3,2],[2,-6]])))
print("*"*100)
print(svd.ortho_3d([[1,1,0],[1,1,1],[0,2,1]]))