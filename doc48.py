'''Write a Python program to split a given list into specified sized chunks. 
Original list:
[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
Split the said list into equal size 3
[[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
Split the said list into equal size 4
[[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
'''
a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
size=int(input("enter the lsub list size:"))
i=0
b=[]
g=[]
while i<len(a):
          c=a[i:i+size]
          b.append(list(c))
          i=i+size
print(b)
