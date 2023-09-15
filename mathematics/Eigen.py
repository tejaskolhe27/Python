import numpy as np
from numpy import linalg as la

c= ([[3,-4],[2,-6]])
d= ([[5,-10,-5],[2,14,2],[-4,-8,6]])

v,w = la.eig(d)

print("Eigen Values are  = ",v)
print("Eigen Vector are = ",w)



