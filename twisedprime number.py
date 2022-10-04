a=int(input("enter the number:"))
b=int(input("enter the number:"))
while a<=b:
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        d=a
        i=0
    while d>0:
        r=d

          