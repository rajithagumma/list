a="my name is rajitha"
b=a.split()
i=0
c=[]
l=""
while i<len(b):
          d=b[i]
          e=d[0].upper()
          k=d.replace(d[0],e)
          l=l+k
          l=l+" "
          i=i+1
c.append(l)
print(c)
print(l)

a=int(input("enter the number:"))
b=int(input("enter the number:"))
d=[]
while a<=b:
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        d.append(a)
    a=a+1
print(d)
k=0
h=[]
while k<len(d):
    g=d[k]
    j=0
    while g>0:
        r=g%10
        j=j*10+r
        g=g//10
    l=d[k],j
    h.append(list(l))
    k=k+1
print(h)

# user=input("enter the user:")
# i=0
# b=[]
# c=1
# while c<len(user):
#     if user[i]!=user[c]:
#         b.append(user[i])
#     c+=1
#     i=i+1
# b.append(user[i])
# print(b)





user=["a","b","a","a","d","c","c","f"]
i=0
b=""
c=1
while c<len(user):
    if user[i]!=user[c]:
        b=b+user[i]
    c+=1
    i=i+1
b=b+user[i]
print(b)



    




