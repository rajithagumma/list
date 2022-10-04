# a="rajitha"
# b=2.0
# c=2
# d=int(b)
# e=c+d
# f=a+str(e)
# g=str(f)
# print(repr(g))


# a="Rajitha"
# a+="Gumma"
# print(a)


# a="this is a string"
# for i in a:
#     if i!=" ":
#         print(i,end="")
#     else:
#         print()


# a=[4,3,2,8]
# [12,6,16]
# i=0
# b=[]
# while i<len(a)-1:
#     p=a[i]*a[i+1]
#     b.append(p)
#     i=i+1
# print(b)





# a=[1,2,3]
# [print(i*2,end=" ")for i in a]


# name=[3,2,4]
# i=0
# b=[]
# target=int(input("enter the target:"))
# while i<len(name):
#     j=1
#     while j<len(name):
#         if name[i]+name[j]==target and name[j]>name[i]:
#             b.append(i)
#             b.append(j)
#         j=j+1
#     i=i+1
# print(b)



# a="Tamanna"
# b=2.0
# c=2
# d=int(b)
# e=c+d


# list1=[1,2,4]
# list2=[1,3,4]
# i=0
# b=[]
# while i<len(list1):
#     b.append(list1[i])
#     b.append(list2[i])
n=int(input("enter the number:"))
m=int(input("enter the number:"))
for i in range(n,m+1):
    factors=0
    for j in range(1,i+1):
        if i%j==0:
            factors=factors+1
    if factors==2:
        print(i)

