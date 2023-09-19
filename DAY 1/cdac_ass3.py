classes_held=int(input("Enter the number of classes held:"))
attended=int(input("Enter the number of classes you have attended:"))
percentage= (attended/classes_held)*100
cause = input("""Is there any Medical Cause?
              Y = Yes
              N = No """)
if cause=='Y':
    print("Allowed to sit in exam")
elif cause=='N':
    print("Percentage of classes attended= ",percentage)
    if percentage<=75:
        print("Not allowed to sit in exam")
    else:
        print("Allowed to sit in exam") 
else:
    print("Invalid input")
