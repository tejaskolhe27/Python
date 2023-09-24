import numpy as np
from scipy.special import cbrt,comb,perm
x=cbrt([27,64])
print(type(x))
print(x)

print(perm(6,2))
print(comb(6,2))

from scipy import stats
m=np.array([[22,13,23,22,56],
            [22,46,45,13,13]])
mod=stats.mode(m,axis=1)
print(mod)

from scipy import integrate
#take f(x) function as f
f= lambda x:x**2
#single integration with a=0, b=1
integration=integrate.quad(f,0,1)
print(integration)