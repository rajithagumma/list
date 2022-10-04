'''List product excluding duplicates.
	List = [6,1,3,5,6,3,1]
	Output: 60'''

a= [6,1,3,5,6,3,1]
i=0
p=1
b=[]
while i<len(a):
          c=a[i]
          if c not in b:
                    b.append(c)
                    p=p*c
          i=i+1
print(p)

