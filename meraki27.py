num=[50,40,23,70,56,12,5,10,7]
a=len(num)
i=0
c=0
while i<a:
    b=num[i]
    if b>20 and b<40:
        c=c+1
    i=i+1
print(c)