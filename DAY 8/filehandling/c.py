import re
with open("productdata.txt","r")as fh: 
    with open("c.txt","w") as fh1:
        dept=input("Enter the category: ")
        for line in fh:
            if re.search(dept,line)!=None:
                fh1.write(line)