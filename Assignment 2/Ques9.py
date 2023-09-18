def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)

x=int(input("Input the value of x: "))
n=int(input("Enter the number of terms: "))
sum=0
for i in range(1,n):
    sum=sum + (x**i/fact(i))
sum=sum+1
print("Sum is: ",sum)