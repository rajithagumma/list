'''You will be given a number and you need to return it as a string in Expanded Form. For example:
12  # Should return '10 + 2'
42 # Should return '40 + 2'
70304  # Should return '70000 + 300 + 4'
'''
a=int(input("enter the length"))
b=[]
i=0
while i<a:
    x=int(input("enter the number"))
    b.append(x)
    num=b[i]
    n=num*1
    r=num%1000
    m=r%100
    y=m%10
    i=i+1
    print('"',n-r,"+",r-m,"+",m-y,"+",y,'"')


