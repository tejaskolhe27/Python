import re

fh = open("mydata.txt")

lst=[]
for line in fh:
    line= line.rstrip("\n")
    print(line)
    lst.append(line)
print(lst)

fh = open("mydata.txt","r")
fh1 = open("copyfile.txt","w")

for line in fh:
    if re.search("game",line)!=None:
        fh1.write(line)

fh.close()
fh1.close()


with open("mydata.txt","r") as fh:
    with open("copyfile.txt","w") as fh1:
        for line in fh:
            lst=line.split(":")
            if lst[2]=="game":
                fh1.write(line)
                