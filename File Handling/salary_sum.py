with open("newdata.txt","r") as fh:
    s=set()
    for line in fh:
       line=line.rstrip("\n")
       l=line.split(":")
       s.add(l[4])
    print("The sum of salaries department wise is:")
    for dept in s:
        s1=0
        fh.seek(0)
        for line in fh:
            line=line.rstrip("\n")
            l=line.split(":")
            if l[4]==dept:
                s1=s1+int(l[3])
        print(dept,"--->",s1)