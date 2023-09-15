#display menu to user for addition of 2 nos, find factorial

def addition(n1,n2):
    return n1+n2

def fact(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    return f


choice=0
while choice!=3:
    print("""
    Enter the choice:
    1. Addition
    2. Factorial
    3. Exit""")
    choice = int(input("    "))

    if choice ==1:
        n1= int(input("ENter 1st number:"))
        n2=int(input("Enter 2nd Number:"))

        s= addition(n1,n2)
        print("Sum=",s)
    elif choice==2:
        n=int(input("Enter the number to get factorial:"))
        ans=fact(n)
        print("The factorial is: ", ans)
    elif choice==3:
        print("Exit")
    else:
        exit()