def palindrome():
    s=input("Enter a string to check palindrome: ")
    print("Original string is: ")
    bad_chars=["'","!","?",",",".",":",";"," "]
    for i in bad_chars:
        s = s.replace(i,'')
        s=s.lower()
    print(s)

    if s==s[::-1]:
        print("Yes it is a palindrome string!!")
    else:
        print("No it is not a palindrome string")

palindrome()
