import numpy as np
from numpy import linalg as la

from sklearn.metrics.pairwise import cosine_similarity 

a=np.array([1,3,2])
b=np.array([2,7,10])

# cosine similarity: cos=a.b/(|a|.|b|)   
#|a|= np.sqrt(np.sum(a*a))

cos= np.dot(a,b)/ ((la.norm(a))*(la.norm(b)))
#print(cos)

print(cosine_similarity([a,b]))

