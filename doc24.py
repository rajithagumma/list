'''Remove duplicates from a list.
List = [1,2,3,1,2,2]
Output: [1,2,3]'''


a=[1,2,3,1,2,2]
i=0
c=[]
while i<len(a):
          b=a[i]
          if b not in c:
                    c.append(b)
          i=i+1
print(c)