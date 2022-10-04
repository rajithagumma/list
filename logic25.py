a=[12,83,73,84]
i=0
b=[]
while i<len(a):
          c=str(a[i])
          print(c)
          j=0
          sum=0
          while j<len(c):
                    d=c[j]
                    sum=sum+int(d)
                    j=j+1
          b.append(sum)
          i=i+1
print(b)

