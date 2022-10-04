l1=[1,2,3,4,5]
l2=[2,3,1,0,6,7]
i=0
a=[]
while i<len(l1):
    b=l1[i]
    if b not in l2:
        a.append(b)
    i=i+1
print(a)