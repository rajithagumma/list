a=[1,1,2,3,4,4,5,1]
i=0
c=[]
index=1
while i<len(a)/2:
          count=a[i]+a[index]
          c.append(count)
          c.append(a[i])
          i=i+1
          index+=1
print(c)
          
