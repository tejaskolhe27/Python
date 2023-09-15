import numpy as np
from numpy import linalg as la

a=np.array([[3,5],[2,3]])
b = np.array([[1,0],[0,0]])
rank= la.matrix_rank(b)
print("Rank: ",rank)