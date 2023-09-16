i=1
sum=0
avg=0
while(i>0):
    n=int(input("Enter the number:"))
    q=input("Do you want to quit??")
    if q=='q':
        sum=sum+n       
        break
    else:
        sum=sum+n
        continue
avg=sum/n
    
print("Sum= ",sum)
print("Avg= ",avg)