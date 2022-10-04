a=int(input("enter the number"))
i=a
while i>=10:
          sum=0
          b=i%10
          sum=sum+b**2
          i=i//10
i=sum
while sum>a:
          c=i%10
          sum=sum+c**2
          i=i//10
i=sum       
if sum==1:
          print("happy number")
else:
          print("no")              

