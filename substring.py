s= input("Enter a string:")
substr=input("Enter the word to find:")
pos=s.find(substr)
print(f"The position of '{substr}' in the sentence is:")
while pos!=-1:
    print(pos)
    pos=s.find(substr,pos+1)

print("The number of occurrence of the word is: ", s.count(substr))