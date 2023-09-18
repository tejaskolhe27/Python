def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

for i in range(1,21):
    print(i,fact(i))