'''Write a Python program to find the list with maximum and minimum length.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])

'''
a=[[1,5,7],[0],[9, 11,6,7,8], [6, 15, 17]]
i=0
max=0
min=10
while i<len(a):
          b=a[i]
          c=len(b)
          if c>max:
                    max=c
                    e=a[i]
          elif c<min:
                    min=c
                    d=a[i]
          i=i+1

print("list lenth maximum",(
print("list lenth minimum","(",min,",",d,")")

