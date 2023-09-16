n=int(input("Enter the number: "))
s=0
count=0
while(n>0):
    d=n%10
    n=n//10
    s=s+d 
    count=count+1
print("The number of digits are: ",count)
print("Sum of the digits are: ",s)
