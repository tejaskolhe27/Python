import numpy as np
from numpy import linalg as la

from sklearn.metrics.pairwise import cosine_similarity 


item1 = np.array([-0.89,0.2,0.8])
item2 = np.array([0.2,0.4,0.5])
item3 = np.array([0.3,-0.9,0.3])
item4 = np.array([0.4,0.23,0.4])
item5 = np.array([0.34,0.3,-0.1])

cos= cosine_similarity([item1,item2,item3,item4,item5])

print(cos)