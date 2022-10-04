name=['n','i','t','i','n']
same=name
index=-1
a=[]
while index>=-len(name):
    num=name[index]
    a.append(num)
    #print(num)
    index-=1
if a==same:
    print(a,"it is polindrome")
else:
    print(a,"it is not polindrome")