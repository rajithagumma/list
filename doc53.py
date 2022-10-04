
check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
print(check2)
check3 = check1[:]
print(check3)
 
check2[0] = 'Code'
print(check2)
check3[1] = 'Mcq'
print(check3)
 
count = 0
for c in (check1, check2, check3):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'Mcq':
        count += 10
 
print (count)


