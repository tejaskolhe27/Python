lst=[1,2,3]
d= dict.fromkeys(lst,10)
print(d)
print(len(d))
print()
d1={"a":10,'b':20,'c':30}
d2={'a':20,'d':40}
d1.update(d2)
print(d1)
print()
d3={**d1,**d2}
print(d3)
print("*"*50)

dic={'DBDA':(100,60),'DAI':(200,50)}
print(len(dic))
print()

dic['DAC']=(200,240)
print(len(dic))
print(dic)
print()

dic1={(1,2):'xxx',(3,4):'yyy'}
print(dic1[(1,2)])
print("*"*50)

v=dic.setdefault("DBDA111",-1)
if v==-1:
    print("Not found")
else:
    print("key found")

print(dic)
dic.popitem()
print("AFTER POPPING: ")
print(dic)
print()
for k in dic.keys():
    print(f"{k}----->{dic[k]}")
print()
for k,v in dic.items():
    if v[0]>100:
        print(k,"------->",v)

print(dic.values())
print(dic)