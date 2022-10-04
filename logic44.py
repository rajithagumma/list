a=["abc","1221","146","111","xyz"]
i=0
c=0
while i<len(a):
          b=a[i]
          if b[0]==b[-1]:
                    c=c+1
          i=i+1
print(c)

a=[1,2,3,1,2,3,7]
i=0
c=[]
while i<len(a):
          b=a.count(a[i])
          if b==1:
                    c.append(a[i])
          i=i+1
print(c)
