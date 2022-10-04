'''Our task is to print the element which occurs 3 consecutive times in a Python list.
Example:
Input: [4, 5, 5, 5, 3, 8]
Output: 5
Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
Output: 1, 22

'''
a=[4,6,4,3,3,4,3,4,3,8]
b=[]
for i in a:
    n=a.count(i)
    if n>3:
        if b.count(i)==0:
            b.append(i)
print(b)
