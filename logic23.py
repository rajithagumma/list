from dataclasses import replace


a="my name is rajitha"
string=""
i=0
while i<len(a):
      if a[i]==" ":
          c=a[i].replace(" ","-")
          string=string+c
      else:
          string=string+a[i]
      i=i+1
      
print('"'+string+'"')
a="my name is tamanna"
b=a.replace(" ","-")
print(b)


