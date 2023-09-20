str=input("Enter a string of odd length with length greater than 7:\n")

l=len(str)
start=int((l-1)/2)
print(str[start-1:start+2])
