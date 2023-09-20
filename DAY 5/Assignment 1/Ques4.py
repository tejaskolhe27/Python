list1 = ["Hello ", "Welcome "]
list2 = ["Students", "Sir"]
list3 = []
# output = [x+y for x in list1 for y in list2]
# print(output)

for i in list1:
    for j in list2:
        output=i+j
        list3.append(output)
print(list3)
               


