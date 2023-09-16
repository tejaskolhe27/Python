a=12
b=a
c= int(input("Enter the number"))
print(id(a),id(b),id(c))
# id for the String will not be same
s = "Hello"
y =s
z = input("Enter the string")
print(id(s),id(y),id(z))



