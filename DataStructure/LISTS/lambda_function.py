lst=[12,23,4,10,99,24,66,76]
print('List is: ',lst)

lst2=list(filter(lambda x:x%2==0,lst))
print("Even elements are: ",lst2)


def  f(n):
    # n=n+10
    return n%2==0 and n>15 and n<70

lst3=list(filter(lambda x:f(x),lst))
print(lst3)