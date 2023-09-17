def add(num):
    if num==1:
        return 1
    else:
        return num+fact(num-1)

def fact(num):
        if num==1:
           return 1
        else:
            return num*fact(num-1)


n=int(input("enter number to find factorial: "))
print(fact(n))

a=int(input("Enter number: "))
print(add(a))