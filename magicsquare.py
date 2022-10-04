a=[[1,2,9],
  [6,7,2],  
  [2,3,4]]
i=0
while i<len(a):
    j=0
    sumr=0
    while j<len(a[i]):
        sumr=sumr+a[i][j]
        j=j+1
    i=i+1
print(sumr)
i=0
while i<len(a):
    j=0
    sumc=0
    while j<len(a[i]):
        sumc=sumc+a[j][i]
        j=j+1
    i=i+1
print(sumc)
i=0
r=2
m=0
while i<len(a):
    j=2
    while j<len(a):
        m+=a[i][r]
        j=j+1
        r=r-1
    i=i+1
print(m)
i=0
p=0
n=0
while i<len(a):
    j=2
    while j<len(a):
        n+=a[i][p]
        j=j+1
        p=p+1
    i=i+1
print(n)
if sumr==sumc==m==n:
    print(a,"it is a magic square")
else:
    print(a,"it is not a magic square")
    


        


            

          
