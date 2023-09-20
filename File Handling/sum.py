s=0
with open("mydata.txt","r") as fh:
    for line in fh:
        lst=line.split(":")
        s=s+int(lst[4])
print("Sum of salary is: ",s)
                