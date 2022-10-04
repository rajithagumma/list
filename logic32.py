a=[1,2,3,4,5,6]
j=-1
i=0
b=[]
while i<3:
    n=a[i]
    f=a[j]
    b.append(f)
    b.append(n)
    i=i+1
    j=j-1
print(b)