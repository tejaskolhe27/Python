def str(s1,s2):
    s=""
    c=len(s2)-1
    for i in s1:
        s=s+i
        s=s+s2[c]
        c=c-1
    return s


s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
print(str(s1,s2))