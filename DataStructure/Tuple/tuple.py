def addition(a=1,b=2,c=4,*t):
    s= a+b+c
    print(t)
    for n in t:
        s= s+n
    return s

print(addition(1,2,3,4,7,2,3,4,5))

