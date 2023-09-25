s=set()
n=int(input("Enter the length of set: "))
for i in range(n):
    a=input("Enter names: ")
    s.add(a)
print("Names are: ",s)

def delete_element():
    delete=input("Enter name to delete: ")
    if delete in s:
        s.remove(delete)
        print("Deleted successfully")
    else:
        print("Exception")
        print(s)

def newset():
    
    return s1

ch=0
while ch!=8:
    ch=int(input("""
    1. delete element if exists otherwise do not show any element
    2. add a element
    3. create one more set
    4. union of 2 sets
    5. intersection of 2 sets
    6. difference of 2 sets
    7. convert set into frozenset
    8. exit
    choice: """))


    match ch:
        case 1:
            delete_element()
        
        case 2:
            a=input("Enter names: ")
            s.add(a)
            print("Succesfullyt added new element")
            print("Updated set is: ",s)
        
        case 3:
            s1=set()
            n=int(input("Enter the length of set: "))
            for i in range(n):
                a=input("Enter elements of new set: ")
                s1.add(a)
            print("New set is: ",s1)
        
        case 4:
            print('The union of two sets is: \n', s.union(s1))
        
        case 5:
            print("The intersection of two sets is: \n", s.intersection(s1))
        
        case 6:
            print("The difference of 2 sets is: \n", s.difference(s1))

        case 7:
            frozen_set=frozenset(s)
            print('The frozen set is: ', frozen_set)
        
        case 8: 
            print("Thank you!!!")