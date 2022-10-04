'''Write a Python program to find the last occurrence of a specified item in a given list.
Original list:
['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
Last occurrence of f in the said list:
7
Last occurrence of c in the said list:
15
Last occurrence of k in the said list:
14
Last occurrence of w in the said list:
12'''

a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(a):
          if a[i]=="f":
                    b=i
          elif a[i]=="c":
                 c=i
          elif a[i]=="k":
                    d=i
          elif a[i]=="w":
                    e=i
          i=i+1

print("last occurence of f is",b)
print("last occurence of f is",c)
print("last occurence of f is",d)
print("last occurence of f is",e)

