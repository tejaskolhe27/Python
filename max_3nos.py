x=int(input("Enter x="))
y=int(input("Enter y="))
z=int(input("Enter z="))

if (x>y and x>z):
    print(x,"is a maximum")
elif (y>x and y>z):
    print(y,"is maximum")
else:
    print(z,"is maximum")
