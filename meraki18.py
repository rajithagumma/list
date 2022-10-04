e=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c_all=0
all_sum=0
evens=0
ce=0
odds=0
co=0
i=0
while i<len(e):
          c_all+=1
          all_sum+=e[i]
          if e[i]%2==0:
                    evens+=e[i]
                    ce+=1
          else:
                    odds+=e[i]
                    co+=1
          i=i+1
avg_all=all_sum/c_all
avg_even=evens/ce
avg_odd=odds/co
print("number of elements",c_all)
print("sum pf all numbers",all_sum)
print("average of all number",avg_all)
print("even numbers",ce)
print("sum of even numbers",evens)
print("average of even numbers is ",avg_even)
print("odd numbers",co)
print("sum of odd numbers",odds)
print("average of odd numbers is ",avg_odd)
