'''Write a Python program to compute the average of nth elements in a given list of lists with different lengths.
Original list:
[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
Average of n-th elements in the said list of lists with different lengths:
[4.8, 5.8, 6.8, 8.0, 11.0]'''

a1=[[0,1,2,], [2, 3, 4,], [3, 4, 5, 6,],[7, 8, 9, 10, 11], [12, 13, 14,]]
a=[[0,1,2,"",""], [2, 3, 4,"",""], [3, 4, 5, 6,""],[7, 8, 9, 10, 11], [12, 13, 14,"",""]]
i=0
c=[]
i=0
while i<len(a):
          j=0
          sum=0
          k=0
          while j<len(a):
                    b=a[j][i]
                    if type(b)==int:
                              sum=sum+b
                    if b=="":
                              k=k+0
                    else:
                              k=k+1              
                    j=j+1
          avg=sum/k
          c.append(avg)
          i=i+1
print(c)


