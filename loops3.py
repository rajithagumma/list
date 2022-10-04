n=int(input("enter the number of rows:"))
i=1
while i<n:
          j=1
          while j<=3:
                    if j==1 or (j==1 and i!=1 and i!=5) or (j==3 and i==3):
                              print("*",end=" ")
                    j=j+1
          i=i+1
          print()