import numpy as np
from numpy import linalg as la

a=np.array([2,-3,6])
b=np.array([8,2,-3])


#L2 Normal: squareroot of the square of the values in vector

norm = np.sqrt(np.sum(a*a))
print(norm)
print(la.norm(a))

#L1 Normal: sum of the abslute values of the vector

l1=la.norm(a,1)
print("L1 norm is ",l1)
