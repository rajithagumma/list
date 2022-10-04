'''Convert Character Matrix to single String;
The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
The String after join: gfgisbest'''
a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
c=""
while i<len(a):
          b=a[i]
          j=0
          while j<len(b):
                    e=b[j]
                    c=c+e
                    j=j+1
          i=i+1
print(c)

