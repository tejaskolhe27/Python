price=  int(input("Enter the price of vehicle"))

if price>100000:
    tax = 15
    insurance = 20
    final = price + 0.2*price + 0.15*price
    print("Tax = ",tax, "%")
    print("Insurance= ",insurance,"%")
    print("The final price is= ",final)
elif price>50000 and price<=100000:
    tax = 10
    insurance = 8
    final = price + 0.08*price + 0.1*price
    print("Tax = ",tax, "%")
    print("Insurance= ",insurance,"%")
    print("The final price is= ",final)
elif price<=50000:
    tax = 5
    insurance = 5
    final = price + 0.05*price + 0.05*price
    print("Tax = ",tax,  "%")
    print("Insurance= ",insurance,"%")
    print("The final price is= ",final)