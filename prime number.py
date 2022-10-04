a=int(input("enter the number:"))
b=int(input("enter the number:"))
h=[]
f=[]
while a<=b:
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        d=a
        h.append(d)
        j=0
        while d>0:
            r=d%10
            j=j*10+r
            d=d//10
        k=j
        m=1
        count=0
        while m<=k:
            if k%m==0:
               count=count+1
            m=m+1
        if count==2:
            f.append(k)
    a=a+1
print("prime numbers is",h)
print("twisted prime numbers is",f)







