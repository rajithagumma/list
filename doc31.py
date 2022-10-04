'''Given the start and end of a range, write a Python program to print all negative numbers in a given range.
Example:
Input: start = -4, end = 5
Output: -4, -3, -2, -1

Input: start = -3, end = 4
Output: -3, -2, -1
'''
s=int(input("enter the starting point:"))
e=int(input("enter the end point:"))
a=[]
while s<=e:
          if s<0:
                    a.append(s)
          s=s+1
print(a)