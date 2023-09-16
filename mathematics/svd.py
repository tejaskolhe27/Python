import numpy as np
from numpy import linalg as la

def ortho_2d(x):
    v1= x[0]
    v2 = x[1]
    u1 = v1/la.norm(v1)
    w2 = v2 - np.dot(u1,v2)*u1
    u2 = w2/la.norm(w2)

    ona = np.array([u1,u2])

    return ona

def ortho_3d(x):
    v1= x[0]
    v2 = x[1]
    v3 = x[2]
    u1 = v1/la.norm(v1)
    w2 = v2 - np.dot(u1,v2)*u1
    u2 = w2/la.norm(w2)
    w3 = v3 -np.dot(u1,v3)*u1 -np.dot(u2,v3)*u2
    u3 = w3/la.norm(w3)
    return np.array([u1,u2,u3])
