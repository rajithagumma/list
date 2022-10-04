'''Write a Python program to convert a given list of strings into list of lists. 
Original list of strings:
['Red', 'Maroon', 'Yellow', 'Olive']
Convert the said list of strings into list of lists:
[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

'''
a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
b=[]
while i<len(a):
          c=a[i]
          d=list(c)
          b.append(d)
          i=i+1
print(b)






