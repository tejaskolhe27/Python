import numpy as np


a=np.arange(12)
b=np.arange(0,48,3).reshape(4,4)

print(a)
print(b)
print(b[1:3,2:4])
print(b[1,-1])

c=np.arange(1,17).reshape(4,4,order='f') #f:to interchange rows and columns
print(c)

d=np.zeros((3,2),dtype='int32')
e = np.ones((3,2),dtype='int32')

print(e)
print(d)

#sum
print(b+c)

#IDENTITY MATRIX
a=np.identity(3)
print(a)
b=np.eye(3,5,k=2)
print(b)

#FILTER THE ARRAY
x= np.array([[1,2,3],[3,4,5],[6,54,4]])
print(x[x%3==0])
print(x[x>2])

#to search the value
print(list(np.where(x%3==0)[0].data))

#to find sum
print(np.sum(x,axis=1))      #row wise sum
print(np.sum(x,axis=0))      #column wise sum
print(np.sum(x))             #total sum of all elements

#mean
print(np.mean(x))

#hstack adn vstack
a=np.array([10,20,30])
b=np.array([11,21,31])
c=np.array([13,23,33])
print(np.hstack((a,b,c)))
print(np.vstack((a,b,c)))

#reverse rows and columns
print(np.flip(x))        #reverse rows&columns
print(np.flip(x,axis=0)) #reverse rows
print(np.flip(x,axis=1)) #reverse columns

#endpoint-false will exclude 30
x=np.linspace(10,30,7,endpoint=False)
print(x)