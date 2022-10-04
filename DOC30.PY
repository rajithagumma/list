'''Given a list of numbers, write a Python program to count positive and negative numbers in a List.
Example:
list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3

Iist2 = [-12, 14, 95, 3]
Output: pos = 3, neg = 1

'''
a=[2,-7,5,-64,-14,-9,-6,8,9]
i=0
p=0
n=0
while i<len(a):
          if a[i]>0:
                    p=p+1
          else:
                    n=n+1
          i=i+1
print("positive numbers is",p)
print("negative numbers in",n)