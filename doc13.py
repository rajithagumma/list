a=[1,1,2,3,4,4,5,1]
# a=list('aabcddddadnss')
b=[]
i=0
while i<len(a):
    count=0
    k=a[i]
    c=[]
    j=0
    while j<len(a):
        l=a[j]
        if k==l:
          count+=1
        j+=1
    c.append(k)
    c.append(count)
    if c not in b:
      b.append(c)
    i+=1
print(b)
    
        
        

