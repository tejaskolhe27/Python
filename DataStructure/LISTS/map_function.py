lst = [1,23,35,47,235,7,46]
lst1=[]
for num in lst:
    lst1.append(num+10)
print(lst1)

lst1 = [num+10 for num in lst ]
print(lst1)

#MAp function

lst1=list(map(lambda x:x+10,lst))
print(lst1)
