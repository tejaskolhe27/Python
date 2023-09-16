lst= [1,2,3,4]
lst1 = ["Pune","Mumbai","Kolkata","Delhi"]

for val in zip(lst,lst1):
    print(val)

for x,y in zip(lst,lst1):
    print(x,"---",y)

print("*"*50,"enamurate","*"*50)
for pos,val in enumerate(lst):
    if val%2==0:
        print(pos,"----",val)

print("*"*50)

l=[12,1,3,14,25]
#to find all even numbers
l1=[]
print("The even numbers in the list are:")
for num in l:
    if num%2==0:
        l1.append(num)

print(l1)

l1=[num for num in l if num%2==0]
print(l1)   
