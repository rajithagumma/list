# a=[50,40,23,70,56,12,5,10,7]
# i=0
# min=1000
# max=0
# secondmax=0
# thirdmax=0
# while i<len(a):
#     num=a[i]
#     if num>max:
#         max=num
#     elif num>secondmax:
#         secondmax=num
#     elif num>thirdmax:
#         thirdmax=num
#     elif num<min:
#         min=num
#     i=i+1
# print(max)
# print(secondmax)
# print(thirdmax)
# print(min)
list=[1,10,15,50,20,24,121,30,40]
max=list[0]
sec_max=list[0]
third_max=list[0]
min=1000
i=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    elif list[i]<min:
        min=list[i]
    i=i+1
i=0
while i<len(list):
    if list[i]>sec_max and list[i]!=max:
        sec_max=list[i]
    i=i+1
i=0
while i<len(list):
    if list[i]>third_max and list[i]!=max and list[i]!=sec_max:
        third_max=list[i]
    i=i+1
print(max)
print(sec_max)
print(third_max)
print(min)