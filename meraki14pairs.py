num=30
n=[10,11,12,13,14,17,18,19]
i=0
while i<len(n):
          j=i+1
          while j<len(n):
                    if n[i]+n[j]==num:
                              print(list((n[i],n[j])),end=" ")
                    j=j+1
          i=i+1

