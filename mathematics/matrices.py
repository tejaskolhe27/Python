import numpy as np
from numpy import linalg as la


v=np.array([[1,2,-3],[0,-4,1]])
u=np.array([[3,2,1],[0,1,0]])
print("Additon is\n", u+v)

#hadamard product

print("Hadamard product:\n",u*v)
#OR print(np.multiply(u,v))

#matrix multiplication

a=np.array([[1,3],[2,-1]])
b=np.array([[2,0,-4],[3,-2,6]])
print("AB=\n",a@b)
print("AB=\n",np.matmul(a,b))