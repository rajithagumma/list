money= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
crorepati=0
lakhpati=0
diwale=0
i=0
while i<len(money):
          if money[i]>=10000000:
                    crorepati+=1
          elif money[i]>=100000:
                    lakhpati+=1
          else:
                    diwale+=1
          i=i+1
print(crorepati,"crorepati")
print(lakhpati,"lakhpati")
print(diwale,"diwale")