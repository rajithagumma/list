'''Write a Python program to sum two or more lists, the lengths of the lists may be different. 
Original list:
[[1, 2, 4], [2, 4, 4], [1, 2]]
Sum said lists with different lengths:
[4, 8, 8]'''

a=[[1, 2, 4], [2, 4, 4], [1, 2,0]]
i=0
c=[]
while i<len(a):
          j=0
          sum=0
          while j<len(a):
                    b=a[j][i]
                    sum=sum+b
                    j=j+1
          c.append(sum)
          i=i+1
print(c)