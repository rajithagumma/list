'''Given a List, extract all elements whose frequency is greater than K.
Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
Output: [4, 3]
Explanation: Both elements occur 4 times.
Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
Output: [4, 3, 6]
Explanation: Occur 4, 3, and 3 times respectively.
'''
a=[4,6,4,3,3,4,3,4,3,8]
b=[]
for i in a:
    n=a.count(i)
    if n>3:
        if b.count(i)==0:
            b.append(i)
print(b)