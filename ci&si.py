principal=float(input("Enter principal="))
rate=float(input("Enter the rate="))
time=int(input("Enter the time="))

if principal>10000:
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount-principal
    print(ci)
else:
    si=(principal*rate*time)/100
    print(si)
