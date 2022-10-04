'''Find the sum of number digits in List.
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7

The original list is : [15, 81, 11, 234]
List Integer Summation : [6,9,2,9]'''


a=[12,67,98,34]
i=0
d=[]
while i<len(a):
          b=a[i]
          c=str(b)
          j=0
          s=0
          while j<len(c):
                    e=c[j]
                    s=s+int(e)
                    j=j+1
          d.append(s)
          i=i+1
print(d)