a=[[4,3,3],[1,4,3],[9,8,7]]
i=0
r=2
m=0
while i<len(a):
    j=2
    while j<len(a):
        m+=a[i][r]
        j=j+1
        r=r-1
    i=i+1
print(m)
i=0
r=0
n=0
while i<len(a):
    j=2
    while j<len(a):
        n+=a[i][r]
        j=j+1
        r=r+1
    i=i+1
print(n)
print(m-n)
