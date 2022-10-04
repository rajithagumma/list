a=[1,3,5,7,9,11,0,2,4,6,8,9,0,4,3,0]
i=0
while i<len(a):
          if (i+1)%4==0:
                    a.insert(i+1,20)
          i=i+1
print(a)
