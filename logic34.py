a="Rajitha is singing very loudly"
i=0
b=""
while i<len(a):
          if a[i]!="i" or a[i]!="s":
                    b=b+a[i]
          i=i+1
print(b)
a="rajitha is singing loudly"
i=0
b=a.split()
c=""
while i<len(b):
    if b[i]!="singing":
        c=c+b[i]+" "
    i=i+1
print(c)
