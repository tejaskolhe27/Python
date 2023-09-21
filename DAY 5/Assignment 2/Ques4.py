lst= []
for i in range(5):
    a=input("Enter the location: ")
    lst.append(a)
print("The locations are: ",lst)
lst1 = []
for i in range(5):
    b=input("Enter the cities: ")
    lst1.append(b)
print("The lists are: ",lst1)


for x,y in zip(lst,lst1):
    print(x,"----",y)