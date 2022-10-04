'''The task is to perform the operation of removing all the occurrences of a given item/element present in a list.


Input :
1 1 2 3 4 5 1 2
1
Output :
2 3 4 5 2
Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.
After removing the item, the output list is [2, 3, 4, 5, 2]
Input :
5 6 7 8 9 10
'''
a=[1,1,2,3,4,5,1,2]
b=int(input("enter the number:"))
i=0
c=[]
while i<len(a):
          d=a[i]
          if d!=b:
                    c.append(d)
          i=i+1
print(c)
a="rajitha"
b=5
print("rajitha,"*(b-1)+a)