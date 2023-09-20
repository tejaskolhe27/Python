i=1
sum=0
avg=0
while(i>0):
    n=input("Enter the number:")
    if n=="q":       
        break
    else:
        n=int(n)
        sum=sum+n
        i=i+1
        continue   

print("Sum= ",sum)
print("Avg= ",sum/(i-1))
