def translate(str):
    consonants='bcdfghjklmnpqrstvwxyz'
    for l in str:
        if l in consonants:
            l=l+'o'+l
            print(l,end="")
        else:
            print(l,end="")
    print()
string=input("Enter Any String: ")

translate(string)