a=[[8,3,4],
   [1,5,9],
   [6,7,2]]
for i in range(len(a)):
          sumr=0
          for j in range(len(a[i])):
                    sumr=sumr+a[i][j]
print(sumr)
for i in range(len(a)):
          sumc=0
          for j in range(len(a[i])):
                    sumc=sumc+a[j][i]
print(sumc)
r=2
diagnol1=0
for i in range(len(a)):
          for j in range(2,len(a[i])):
                    diagnol1=diagnol1+a[i][r]
                    r=r-1
print(diagnol1)
r=0
diagnol2=0
for i in range(len(a)):
          for j in range(2,len(a[i])):
                    diagnol2=diagnol2+a[i][r]
                    r=r+1
print(diagnol2)
if sumr==sumc==diagnol1==diagnol2:
          print(a,"it is a magic square")
else:
          print(a,"it is not a magic square")
