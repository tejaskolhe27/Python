with open("productdata.txt","r") as fh:
    s=set()
    for line in fh:
       line=line.rstrip("\n")
       l=line.split(":")
       s.add(l[3])
    print("The sum is:")
    for dept in s:
        s1=0
        fh.seek(0)
        for line in fh:
            line=line.rstrip("\n")
            l=line.split(":")
            if l[3]==dept:
                s1=s1+int(l[4])
        print(dept,"--->",s1)
        
        