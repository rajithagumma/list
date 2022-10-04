e=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
evens=0
ce=0
odds=0
co=0
i=0
while i<len(e):
          if e[i]%2==0:
                    evens+=e[i]
                    ce+=1
          else:
                    odds+=e[i]
                    co+=1
          i=i+1
avg_even=evens/ce
avg_odd=odds/co
print("average of even numbers is ",avg_even)
print("average of odd numbers is ",avg_odd)
