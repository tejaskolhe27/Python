lst=[12, 1, 3, 7, 8, 5, 8]
print("Original list: ",lst)
lst1=[-1]*(max(lst)+1)
print("New swapped list: ")
for i in range(0,len(lst)):
    a=lst[i]
    del lst1[a]
    lst1.insert(a,i)
print(lst1)
