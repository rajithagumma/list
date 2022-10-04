'''Write a Python program to join adjacent members of a given list.
Original list:
['1', '2', '3', '4', '5', '6', '7', '8']
Join adjacent members of a given list:
['12', '34', '56', '78']
Original list:
['1', '2', '3']
Join adjacent members of a given list:
['12']
'''
a=["1","2","3","4","5","6","7","8"]
i=0
b=len(a)
c=[]
while i<b-1:
          d=a[i]
          e=a[i+1]
          f=d+e
          c.append(f)
          i=i+1
print(c)
 