'''For example, if we give 9119  the function should return  811181, as the  
square of 9 is 81 and square of 1  is 1.'''


l=[9119]
b=[]
i=0
while i<len(l):
          n=l[i]
          j=0
          while j<n:
                    r=n%10
                    t=r*r
                    n=n//10
                    print(t,end="")
                    j=j+1
          i=i+1

