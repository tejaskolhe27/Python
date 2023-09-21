"""
Write a menu driven program to practice String functions
Design following meu
a. display characters from even position
b. display characters from odd position
c. display length of a string
d. add a at the end of string length times
e. exit
"""

def evenposition(s):
    print("The characters from even position are: ")
    for i in range (1,len(s)+1):
        if i%2==0:
            print(s[i-1],end=" ")

def oddposition(s):
    print("The characters from odd position are: ")
    for i in range (0,len(s)):
        if i%2==0:
            print(s[i],end=" ")



s=input("Enter a string:")
choice='a'
while choice!='e':
    choice= input("""
    a. display characters from even position
    b. display characters from odd position
    c. display length of a string
    d. add a at the end of string length times
    e. exit 
    choice: """)
                  
    match choice:
        case 'a':
            evenposition(s)
        case 'b':
            oddposition(s)
        case 'c':
            print("The length of string is: ", len(s))
        case 'd':
            print("New updated string: ")
            s=s+'a'*len(s)
            print(s)
        case 'e':
            print("THANKS!!!")