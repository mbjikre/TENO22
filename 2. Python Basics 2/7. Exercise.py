sm = [
    [0,0,0,1,0,0,0],
    [0,0,2,1,3,0,0],
    [0,2,2,1,3,3,0],
    [2,2,2,1,3,3,3],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for col in sm:
    for row in col:
        if row == 1:
            print('/\\', end='')
        elif row == 2:
            print('/', end='')
        elif row == 3:
            print('\\', end='')
        else:
            print(' ', end='')
    print('')

li = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'n', 'm', 'n']
lic = []
for i in li:
    if li.count(i) > 1:
        if i not in lic:
            lic.append(i)

print(lic)
