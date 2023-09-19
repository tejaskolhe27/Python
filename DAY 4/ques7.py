def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)
    
num=int(input("Enter number upto which you want addition: "))
print("The addition is: ")
print(add(num))
    
