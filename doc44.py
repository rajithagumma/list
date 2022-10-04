'''Write a Python program to add a number to each element in a given list of numbers.
Original lists:
[3, 8, 9, 4, 5, 0, 5, 0, 3]
Add 3 to each element in the said list:
[6, 11, 12, 7, 8, 3, 8, 3, 6]'''

a=[3,8,9,4,5,0,5,0,3]
i=0
b=[]
c=int(input("enter the adding element:"))
while i<len(a):
          d=a[i]+c
          b.append(d)
          i=i+1
print(b)
a=[3,8,9,4,5,0,5,0,3]
i=0
b=[]
c=int(input("enter the adding element:"))
while i<len(a):
          d=a[i]+c
          b.append(d)
          i=i+1
print(b)
