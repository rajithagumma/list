# sum of the series
a=[6,2.9,"18.9",40,"50"]
i=0
sum1=0
sum2=0
sum=0
while i<len(a):
          if type(a[i])==str:
                    b=int(float(a[i]))
                    sum2=sum2+b
          elif type(a[i])==float:
                    c=int(a[i])
                    sum1=sum1+c
          else:
                    d=a[i]
                    sum=sum+d
          i=i+1
print(sum1+sum2+sum)