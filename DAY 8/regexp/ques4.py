"""
Write a python program to accept user name and password and validate it. username
should contain only alphabets or digits and password length should be 8, starts with
alphabet and should contain at least one special character(#,@) .
accept username and password from user and validate it. if it is valid then display message
welcome to our application. otherwise ask to re-enter.
(allows maximum 3 attempts to accept password
 """
 
import re
username=input("Enter username: ")
m=re.match("\w+|\d+",username,re.I|re.M)
if m!=None:
    print("Username valid")
else:
    print("Username not valid")

for i in range(3):
    password=input("Enter password: ")
    n=re.match("^\w+\W",password,re.I|re.M)
    
    if n!=None:
        print("Password Valid")
        print("Welcome to our application")
        break
    
    else:
        print("Invalid")
        print(f"You have {2-i} attempts remaining")

#INCOMPLETE
