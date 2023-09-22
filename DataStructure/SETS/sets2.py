sets ={1,2,3,4,5,6}
sets2= {10,20,30,40,1,2,3,100}
#UNION
print(sets.union(sets2))
print(sets|sets2)
print()
#INTERSECTION
print(sets.intersection(sets2))
print(sets&sets2)
print()
#DIFFERENCE
print(sets.difference(sets2))
print(sets-sets2)
print()
#DIFFERENCE_UPDATE  a
#print(sets.difference_update(sets2))

#SYMMETRIC DIFFERENCE
print(sets.symmetric_difference(sets2))
print()

print("superset",sets.issuperset(sets2),sets>sets2)
print("subset",sets.issubset(sets2),sets>sets2)
print("disjoint",sets.isdisjoint(sets2))