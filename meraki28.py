marks=[23,45,67,89,90,25,29,80]
a=len(marks)
i=0
lessthan_50=0
while i<a:
    b=marks[i]
    if b<50:
        lessthan_50+=1
    i=i+1
print(lessthan_50)