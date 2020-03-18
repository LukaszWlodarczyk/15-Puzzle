tab1 = [[2,1],[3,4]]
tab2 = []
for row in tab1:
    tab2.append(row.copy())
print(tab1)
print(tab2)
tab1[0][0], tab1[1][0] = tab1[1][0], tab1[0][0]
print(tab1)
print(tab2)