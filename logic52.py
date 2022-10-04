a=[2,1,7,5,3,8]
i=0
c=[]
k=1
while i<len(a):
          b=a[i]
          e=str(b+k)
          if len(e)>1:
                    f=e[0]
                    g=int(f)
                    c.append(g)
          else:
                    h=int(e)
                    c.append(h)
          i=i+1
          k=k+1
print(c)
