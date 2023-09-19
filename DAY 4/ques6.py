def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

if __name__ == "__main__":
    for i in range(1,21):
        print(i,fact(i))