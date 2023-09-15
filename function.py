def f1():
    x=34
    print(x)
    def f2():
        nonlocal x
        x=45
        print(x)
    print(x)
    f2()
    print(x)
x = 10
print(x)
f1()
print(x)    