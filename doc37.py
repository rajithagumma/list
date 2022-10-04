'''Write a Python program to pair up the consecutive elements of a given list.
Original lists:
[1, 2, 3, 4, 5, 6]
Pair up the consecutive elements of the said list:
[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
'''
a=[1,2,3,4,5,6]
i=0
b=len(a)
c=[]
while i<b-1:
          j=i
          d=[]
          while j<i+1:
                    d.append(a[j])
                    d.append(a[j+1])
                    j=j+1
          c.append(d)
          i=i+1
print(c)