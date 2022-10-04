values = [[3, 4, 5, 1], [33, 6, 1, 2]]
v = values[0][0]
for lst in values:
          for element in lst:
                    if v > element:
                              v = element
                              print(v)