l=[6,1,3,5,6,3,1]
i=0
a=[]
while i<len(l):
    b=l[i]
    if b not in a:
        a.append(b)
    i=i+1
print(a)
product=1
k=0
while k<len(a):
    b=a[k]
    product=product*b
    k=k+1
print(product)