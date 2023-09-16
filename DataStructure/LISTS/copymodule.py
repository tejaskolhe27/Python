#deep copy is only helpful in nested lists and not in regular list, otherwise it is the same as shallow copy

import copy
lst=[10,20,30,[1,2,3]]
lst1 = copy.deepcopy(lst)
lst2=lst.copy()
# print(lst,lst1)
lst[3].append(100)
print(lst,"\n",lst1,"\n",lst2)
