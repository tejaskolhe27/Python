unit=int(input("Enter the unit of electricity:"))
if unit<=100:
    bill=0
    print("The bill is: ", bill)
elif unit>100 and unit<=200:
    bill=unit*5
    print("The bill is: ", bill)
elif unit>200:
    bill=(unit-200)*10+(100*5)
    print("The bill is: ", bill)