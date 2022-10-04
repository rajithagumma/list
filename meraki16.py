e=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
evens=0
odds=0
i=0
while i<len(e):
          if e[i]%2==0:
                    evens+=e[i]
          else:
                    odds+=e[i]
          i=i+1
print("sum of even numbers is ",evens)
print("sum of odd numbers is ",odds)

