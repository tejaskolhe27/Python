import re
mob=input("Enter the mobile number: ")
m = re.match("^\+91-[987]\d{9}$",mob)
if m!=None:
    print("Mobile number is valid")
else:
    print("Not valid number")
print("*"*50)


s="This is home sweet home"
m= re.match("(\w+)\s(\w+)\s(\w+)",s)
if m!=None:
    print(m.group(),":",m.span())
    print(m.group(1),":",m.span(1))
    print(m.group(2),":",m.span(2))
    print(m.group(3),":",m.span(3))
    print("valid")
else:
    print("Not valid")
print("*"*50)

ac="XXXX1234XXXX"
m=re.match("^X{4}(\d{4})X{4}$",ac)
if m!=None:
    print(m.group(1),m.span(1))
    print("VALID")
else:
    print("INVALID")
