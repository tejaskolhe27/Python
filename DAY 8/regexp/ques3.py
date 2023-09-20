"""
Accept lines from user and display only the lines that start with 
a number or any 2 alphabets
"""

import re
mob=input("Enter the mobile number: ")
m = re.match("^[0-9]\d{9}$",mob)
if m!=None:
    print("Mobile number is valid")
else:
    print("Not valid number")