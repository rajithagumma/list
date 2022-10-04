a=[20,8,2,7,78,92,15]
i=0
max=0
min=1000
c=[]
while i<len(a):
          b=a[i]
          if b>max:
                    max=b
          elif b<min:
                    min=b
                    c.append(min)

          i=i+1
print(c)
