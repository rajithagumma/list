l=[1,2,2,5,8,4,4,8]
i=0
a=[]
while i<len(l):
    b=l[i]
    if b not in a:
        a.append(b)
    i=i+1
print(a)
k=0
c=0
while k<len(a):
    c=c+1
    k=k+1
print(c)