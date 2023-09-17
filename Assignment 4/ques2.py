lst=[]
for i in range(0,3):
    a=int(input("Enter the data for histogram: \n"))
    lst.append(a)
print("The histogram is:",lst)
for i in range(len(lst)):
    print("*"*lst[i])