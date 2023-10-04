s1=input("Enter string 1:\n")
s2=input("Enter string 2:\n")

mid=int((len(s1)/2))
x=s1[:mid:]
x=x+s2
x=x+s1[mid:]
print(x)
