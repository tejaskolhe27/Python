def strings(s):
    lower=[]
    upper=[]
    for i in s:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)
    str=''.join(lower+upper)
    return str

s="PytHONStudy"
print("arranging characters giving precedence to lowercase letters: ",strings(s))
