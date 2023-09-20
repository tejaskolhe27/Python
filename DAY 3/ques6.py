s = "Welcome to USA. USA awesome, isn't it?"
l=len(s)
pos=s.find("USA")
print("Position form left to right:")
while pos!=-1:
    print(pos)
    pos=s.find("USA", pos+1)

print("*"*25,"Reverse","*"*25)

#reverse
print("Position from right to left:")
pos=s.rfind("USA")
while pos!=-1:
    print(pos)
    pos=s.rfind("USA",0,pos)