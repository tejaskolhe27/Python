#Accwpt the no. from user till user enters a num which is divisible by 10
#but accept maximum 10 numbers, if user enters all 10 numbers display the additon of all 10 nos otherwise display that you have entered wrong values


s=0
for i in range(0,10):
    num=int(input("Enter number:"))

    if(num%10==0):
        print("You have entered wrong value!!!!")
        break
    s=s+num
else:
    print("The sum is=", s)
