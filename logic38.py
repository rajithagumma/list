# a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# i=0
# c=[]
# d=[]
# while i<len(a):
#           if a[i] not in d:
#                     d.append(a[i])
#                     b=a.count(a[i])
#                     c.append(b)
#                     c.append(a[i])
#           i+=1
#print(c)
a=["RajItHa"]
i=0
c=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if j!=1 and j!=2 and j<=5:
            c.append(j)
        j=j+1
    i=i+1
print(c)