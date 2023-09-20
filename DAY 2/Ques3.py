def hcf(n1,n2):
    hcf=0
    if n1>n2:
        small=n2
    else:
        small=n1
    for i in range(1,small+1):
        if (n1%i==0) and (n2%i==0):
            hcf=i
    return hcf

n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print("HCF is: ", hcf(n1,n2))