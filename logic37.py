# a=["rajitha","tamanna"]
# i=0
# while i<len(a)/2:
#           print(a[i][i],".",a[i+1][i],".")
#           i=i+1
# a=["rajitha","tamanna"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     n=a[i][j]
#     print(n,".",end="")
#     j=j+1
#     i=i+1
a=["rajitha","kook","tamanna","mom"]
i=0
while i<len(a):
    n=a[i]
    r=n[::-1]
    if r==a[i]:
        print("palindrome",r)
    else:
        print("not palindrome",r)
    i=i+1