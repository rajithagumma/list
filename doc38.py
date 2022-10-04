'''Write a Python program to check if a given string contains an element, which is present in a list. 
The original string and list:
https://www.w3resource.com/python-exercises/list/
['.com', '.edu', '.tv']
Check if https://www.w3resource.com/python-exercises/list/ contains an element, which is present in the list ['.com', '.edu', '.tv']
True'''

a="https://www.w3resource.net"
b=['.com', '.edu', '.tv']
i=0
d=0
while i<len(b):
          c=b[i]
          if c in a:
                    d+=1
          i=i+1
if d>=1:
          print("true")
else:
          print("false")