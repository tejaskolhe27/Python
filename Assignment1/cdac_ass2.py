amount= int(input("Enter the amount="))

def calculate(amount):
    n1=amount//2000
    n2=amount%2000
    print("2000 rs notes:", n1)
    if n2<2000:
        n3=n2//500
        n4=n2%500
        print("500 rs notes:", n3)
        if n4<500:
            n5=n4//100
            n6=n4%100
            print("100rs notes:", n5)
            if n6<100:
                n7=n6//50
                n8=n6%50
                print("50rs notes:", n7)
                if n8<50:
                    n9=n8//10
                    n10=n8%10
                    print("10rs notes:",n9)
                    if n10<10:
                        n11=n10//5
                        n12=n10%5
                        print("5rs notes:",n11)
                        if n12<5:
                            n13=n12//2
                            n14=n12%2
                            print("2rs notes:",n13)
                            if n14<2:
                                print("1rs notes:",n14)

if amount>2000:
     calculate(amount)
elif amount<2000:
     calculate(amount)