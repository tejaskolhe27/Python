lst=[12,23,45,66]
lst.append("hello")
print(lst)
print(len(lst))
lst.extend("test")
print(lst)
print(len(lst))
lst.pop()
print(lst)
lst.remove("t")
print(lst)
print(23 in lst)
print(lst.index("s"))
l=[23,1,222,54,6,79]
l.sort()
print(l)

l.sort(reverse=True)
print(l)
l.reverse()
print(l)

l2 = l.copy()
l.append(100)
print(l,l2)
  