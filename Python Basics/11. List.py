greet = 'heellloooo'
greet = greet.replace('l', '!')
print(greet)

fst = ['facebook',
       'amazon',
       'apple',
       'netflix',
       'google']

fst[0] = 'beta'
sst = fst[:]
sst[0] = 'meta'
print(fst)
print(sst)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][:])

li = [1,2,3,4,5]
li.extend([100,101])
#nl = li
print(li)
#print(nl)

nl = li.pop(4)
li.remove(100)
print(li)
print(nl)

li = [1,2,3,4,5]
print(li.index(5))

