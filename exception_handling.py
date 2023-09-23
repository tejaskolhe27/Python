d={"a":10,"b":20}

try:
    a=int(input("Enter number: "))
    print(a)
    print(d['x'])
except ValueError as v:
    print("Invalid entry")
    print(v)
except KeyError as k:
    print("Key not found")
    print(k)
    
def divide(x,y):
    return x/y
try:
    x=int(input("Enter number 1: "))
    y=int(input("Enter number 2: "))
    c=divide(x,y)
    print(c)
except ZeroDivisionError as z:
    print("Cannot divide")
    print(z)