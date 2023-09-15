x=10
print(x,bin(x))
y=15
print(y,bin(y))

newnum=x<<4             #left shift
newx=newnum|y           #OR operator
print(newx,bin(newx))


y1=newx&(int(0b1111))   #AND operator
print("x = ",newx>>4,"y = ",y1)       #right shift