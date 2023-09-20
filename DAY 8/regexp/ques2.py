"""
Accept lines from user and display only the lines that start with 
a number or any 2 alphabets
"""

import re
s=input("Enter: ")
m=re.match("(\d[^0-9]|[a-zA-Z]{2}[0-9])",s,re.I|re.M)
if m!=None:
    print(s)
else:
    print("invalid")
