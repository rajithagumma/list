# i=int(input("enter the number:"))
# b=int(input("enter the number:"))
# while i<b:
for i in range(10,51):
          a=i
          sum=0
          while i>0:
                    r=i%10
                    sum=sum+r
                    i=i//10
          if a%sum==0:
                    print(a,end=",")
          i=i+1