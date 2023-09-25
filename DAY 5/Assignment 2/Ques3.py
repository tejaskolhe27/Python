l=[1,4,3,9,5,7,20]
print("The original list is: ",l)

choice=0
while choice!=9:
    choice=int(input("""
    1. Accept Data
    2. Delete data by value display message deleted successfully or not found
    3. delete data by position
    4. sort
    5. reverse
    6. Print in sorted order without changing original list
    7. print in reverse order without changing original list
    8. display data
    9. Exit
    choice: """))

    match choice:
        case 1:
            ch=input("""
            a) add at last position
            b) add at given position
            Enter choice: """)
            if ch=='a':
                x= int(input("Enter a data to append"))
                l.append(x)
                print("Data added at last positon!")
                print(l)
            elif ch=='b':
                x=int(input("Enter a data to append: "))
                pos=int(input("Enter at which position to append: "))
                l.insert(pos,x)
                print("Data added at last positon!")
                print(l)
        
        case 2:
            d= int(input("Enter value to delete: "))
            if d in l:
                l.remove(d)
                print("DELETED SUCCESSFULLY")
            else:
                print("NOT FOUND")
            print(l)

        case 3:
            ch=input("""
            a) delete last element
            b) delete from particular position
            Enter choice: """)
            if ch=='a':
                l.pop()
            elif ch=='b':
                pos=int(input("Enter the position from where to delete: "))
                l.pop(pos)
            print(l)

        case 4:
              ch=input("""
              a) ascending
              b) descending
              Enter choice: """)
              if ch=='a':
                  l.sort()
              elif ch=='b':
                  l.sort(reverse=True)
              print(l)
        case 5:
            l.reverse()
            print(l)
        case 6:
           print("Sorted List: ",sorted(l))
           print("Original List: ",l)
        
        case 7:
            rl=[]
            for i in reversed(l):
                rl.append(i)
            
            print("Reversed List: ",rl)
            print("Original List: ",l)
        case 8:
            while True:
                print("a. Normal\nb. Numbered\nc.Back")
                ch1=input("Enter a choice: ")
                if ch1=='a':
                    print(l)
                elif ch1=='b':
                    for i in range(len(l)):
                        print(f"{i} {l[i]}")
                elif ch1=='c':
                    break
                else:
                    print("Wrong Choice")

            
        case 9:
            pass