# n=[1,2,3,4,5,6]
# i=0
# j=-1
# b=[]
# while i<3:
#           c=n[i]
#           d=n[j]
#           b.append(d)
#           b.append(c)
#           i=i+1
#           j=j-1
# print(b)

a=["rajitha","tamanna",1,3,"2"]
i=0
b=[]
while i<len(a):
          if type(a[i])==str:
                    b.append(a[i])
          i=i+1
print(b)
