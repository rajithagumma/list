n=int(input("enter the no;"))
i=0
while i<n:
    j=n-i-1
    while j>0:
        print(" ",end=" ")
        j=j-1
    k=i+1
    while k>0:
        print("*",end=" ")
        k=k-1 
    i=i+1
    print()
i=n-1
while i>=1:
    k=1
    while k<=(n+1)-i-1:
        print(" ",end=" ")
        k=k+1
    j=n
    while j>n-i:
        print("*",end=" ")
        j=j-1
    print()    
    i=i-1
# n=int(input("enter the number:"))
# for i in range (n+1):
#     for j in range (n-i,0,-1):
#         print(" ",end=" ")
#     for k in range (0,i):
#         print("*",end=" ")
#     print()
# for i in range (n-1):
#     for k in range(i+1):
#         print(" ",end=" ")
#     for j in range (i,n-1):
#         print("*",end=" ")
#     print()
# i=1
# while i<=6:
#     print("* "*i)
#     i=i+1
# i=5
# while i>=1:
#     print("* "*i)
#     i=i-1