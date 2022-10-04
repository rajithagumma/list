'''Write a Python program to iterate a given list cyclically on specific index position. 
Original list:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Iterate the said list cyclically on specific index position 3 :
['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
Iterate the said list cyclically on specific index position 5 :
['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
'''
a=["a","b","c","d","e","f","g","h"]
b=int(input("enter cyclically on specific index position:"))
c=-(b-2)
d=[]
while c<b:
          d.append(a[c])
          c=c+1
print(d)