a=int(input("enter the number:"))
i=1
n=int(input("enter the nth term:"))
sum=0
while i<=n:
          b=int(str(a)*i)
          sum=sum+b
          print(str(a)*i+"+",end="")
          i=i+1
print()
print(sum)