s="Something is there Somewhere"
import re
m = re.search("s.*e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("Not found")

print("*"*50)    
m = re.search("the",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("Not found")
print("*"*50)  
    
lstmatch = re.finditer("s.*?e",s,re.I|re.M)
if lstmatch!=None:
    for m in lstmatch:
        print(m.group())
        print(m.span())
else:
    print("Not found")
print("*"*50)

lst= re.findall("s.*?e",s,re.I|re.M)
if lst!=None:
        print(lst)
else:
    print("Not found")
print("*"*50)

s1 = re.sub("s.*?e","any",s,flags=re.I|re.M)
print(s1)

print("*"*50)

myreg=re.compile("s.*e",flags=re.I|re.M)
m=myreg.search(s)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("Not found")