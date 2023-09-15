import numpy as np
# np.eye() for identity matrix

b=np.array([[1,3],[5,3]])

fx= 2*np.matmul(b,b) - (4*b)+ (3*np.eye(2))
print(fx)

gx= np.matmul(b,b) - (4*b) - (12*np.eye(2))
print(gx)