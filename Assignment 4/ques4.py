import string
def pangram(str):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in str.lower():
            return False
 
    return True



s=input("Enter a sentence to check pangram: \n")
if pangram(s)==True:
    print("The sentence is pangram")
else:
    print("The sentence is not pangram")