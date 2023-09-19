n= int(input("Enter number of lines: "))
i=n-1
j=0
while(i>=0):
  a=" "*j+"10"*i+"1"+" "*j
  print(a)
  i=i-1
  j=j+1
  if(i<0 and j>=4):
   break
print("*"*50)

