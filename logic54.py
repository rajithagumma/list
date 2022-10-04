a=['Python', 3, 2, 4, 5, 'version']
i=0
max=a[0]
min=a[0]
c=[]
while i<len(a):
        b=a[i]
        if type(b)==int:
            c.append(b)
            if b>max:
                max=b
            elif b<min:
                min=b
        i=i+1
print("maximum number",max)
print("minimum number",min)
print(c)
