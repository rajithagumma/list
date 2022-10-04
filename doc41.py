'''Write a Python program to find the dimension of a given matrix.
Original list:
[[1, 2], [2, 4]]
Dimension of the said matrix:
(2, 2)
Original list:
[[0, 1, 2], [2, 4, 5]]
Dimension of the said matrix:
(2, 3)'''

a=[[0,1,2],[2,4,5]]
i=0
c=[]
while i<len(a):
          b=a[i]
          j=0
          while j<len(b):
                    j=j+1
          i=i+1
c.append(i)
c.append(j)
print("dimension of matrix is",c)