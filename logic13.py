list=["ManJuShA"]
i=0
c=[]
while i<len(list):
          b=list[i]
          j=0
          while j<len(b):
                    if b[j].isupper()==True:
                              c.append(j)
                    j=j+1
          i=i+1
print(c)

