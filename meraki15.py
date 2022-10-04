e=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
evenc=0
oddc=0
i=0
while i<len(e):
          if e[i]%2==0:
                    evenc+=1
          else:
                    oddc+=1
          i=i+1
print("even numbers is ",evenc)
print("odd numbers is ",oddc)

