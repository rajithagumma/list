a=[2,4,4,8,7,7,2,8,9,6,3,9,6]
#[[2,2],[4,2],[8,2],[7,2],[9,2],3,[6,2]]
i=0
b=[]
e=[]
while i<len(a):
    c=a.count(a[i])
    if c>1:
        d=str(a[i])+str(c)
        if d not in e:
            e.append(d)
            b.append(list(d))
    else:
        b.append(a[i])
    i=i+1
print(b)


