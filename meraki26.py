num=[50,40,23,70,56,12,5,10,7]
i=0
max=0
a=len(num)
while i<a:
    b=num[i]
    if b>max:
        max=b
    i=i+1
print(max)