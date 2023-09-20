x=int(input("Enter the value of x: "))
n=int(input("Enter the number of terms: "))
sum=x
m=-1
print("The values of the series are: ")
print(x)
for i in range(1,n):
    ctr = (2 * i + 1)
    nn = (x**ctr) * m
    print(nn)
    sum = sum + nn
    m = -m
print("Sum = ",sum)