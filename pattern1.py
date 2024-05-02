n=int(input("enter a number:"))
for i in range(n):         #rows
    for j in range(i+1):      #column
      print("*",end="")
    print()
