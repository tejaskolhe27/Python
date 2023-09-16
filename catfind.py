s="this is a cat, cat is cute, where is your cat? minr is here"
l=len(s)
pos=s.find("cat")
print("Position form left to right:")
while pos!=-1:
    print(pos)
    pos=s.find("cat", pos+1)

print("*"*25,"Reverse","*"*25)

#reverse
print("Position from right to left:")
pos=s.rfind("cat")
while pos!=-1:
    print(pos)
    pos=s.rfind("cat",0,pos)
    

# for i in range(l):
#     pos=s.find("cat",pos+1)
    
#     print(pos)
#     if pos==-1:
#         break

# for i in range(l):
#     pos=s.rfind("cat",0,pos)
#     print(pos)
#     if pos==-1:
#         break