'''Given start and end of a range, write a Python program to print all positive numbers in given range.
Example:
Input: start = -4, end = 5
Output: 0, 1, 2, 3, 4, 5 

Input: start = -3, end = 4
Output: 0, 1, 2, 3, 4
'''
# s=int(input("enter the starting point:"))
# e=int(input("enter the end point:"))
# a=[]
# while s<=e:
#           if s>0:
#                     a.append(s)
#           s=s+1
# print(a)
i=1
v=1
while i<=3:
          j=1
          while j<=3:
                    if (i==2 and j==1) or (i==2 and j==2):
                              print(v+4,end=" ")
                    elif (i==2 and j==3) or (i==3 and j==2):
                              print(v-2,end=" ")
                    elif (i==3 and j==3):
                              print(v-4,end=" ")
                    else:
                              print(v,end=" ")
                    j=j+1
                    v=v+1
          i=i+1
          print()