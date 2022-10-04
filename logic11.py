l=[10,10,10,20,30,50,20,50,10,12]
i=0
c=0
b=[]
while i<len(l):
    j=1
    while j<len(l):
        if i!=j:
            if l[i]==l[j]:
                e=str(l[i]),str(l[j])
                d=list(e)
        j=j+1
        if d not in b:
            b.append(d)
            c=c+1
    i=i+1
print(c)
print(b)
# l=[1,1,1,1,1,1,1,1,1,1,1]
# i=0
# c=0
# b=[]
# while i<len(l):
#     j=1
#     while j<len(l):
#         if i!=j:
#             if l[i]==l[j]:
#                 e=str(l[i]),str(l[j])
#                 d=list(e)
#         j=j+1
#     b.append(d)
#     c=c+1
#     i=i+1
# print(c)
# print(b)

