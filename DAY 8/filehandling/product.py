import re
with open("productdata.txt","r") as fh:
    with open("a.txt","w") as fh1:
           for line in fh:
            if re.search("^12.*0$",line)!=None:
                fh1.write(line)