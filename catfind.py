s="this is a cat, cat is cute, where is your cat? minr is here"
l=len(s)
pos=0
for i in range(l):
    pos=s.find("cat",pos+1)
    print(pos)
    if pos==-1:
        break

#reverse
for i in range(l):
    pos=s.rfind("cat",pos+1)
    #print(pos)
    