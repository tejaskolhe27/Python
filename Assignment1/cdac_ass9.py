year =  int(input("Enter the year"))

if year%100 == 0 and year%400 == 0:
    print("it is leap year")
else:

    if year%4==0 and year%100!=0:
        print("leap year")
    else:
        print("It is not")