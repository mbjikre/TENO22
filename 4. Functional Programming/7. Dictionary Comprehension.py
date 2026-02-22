exm1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5
}

asi = {k:v*v for k,v in exm1.items() if v%2==0}
print(asi)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

df = list(set([v for v in some_list if some_list.count(v)>1]))
print(df)