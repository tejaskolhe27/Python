"""
write a regex to get only the part of the email before the "@" sign excluding the "@" sign.
example myemail@google.com 
o/p myemail
"""

import re
s ="myemail@google.com"
m=re.match("(\w.*)(@)",s,re.I|re.M)
if m!=None:
    print(m.group(1))
else:
    print("invalid")