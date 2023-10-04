import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([[3,4,5],[6,7,8],[1,2,3],[2,2,2]])
c=np.array([[['a','b','c'],
            ['d','e','f']],
            [['g','h','i'],
            ['j','k','l']]])


print(a)
print("Array type: ",type(a))
print("Data type: ",a.dtype)
print("Dimensions: ",a.ndim)
print("Shape: ", a.shape)

print(b)
print("Array type: ",type(b))
print("Data type: ",b.dtype)
print("Dimensions: ",b.ndim)
print("Shape: ", b.shape)

print(c)
print("Array type: ",type(c))
print("Data type: ",c.dtype)
print("Dimensions: ",c.ndim)
print("Shape: ", c.shape)

from numpy import linalg as la
m=np.array([[10,20],
            [30,40]])
print(la.det(m))

eig_val,eig_vect=la.eig(m)
print(eig_val)
print(eig_vect)