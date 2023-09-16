n=int(input("Enter the number of odd lines: "))
count=n//2
for i in range(1,n+1,2):
    print(" "*count,"*"*i,sep="")
    count=count-1


count=1
for i in range(n-2,0,-2):
    print(" "*count,"*"*i,sep="")
    count =count+1
