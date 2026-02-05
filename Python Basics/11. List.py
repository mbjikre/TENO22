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
print(li.index(3,0,3))

li = ['a', 'b', 'c', 'd', 'e', 'a']
print('a' in li)
print(li.count('a'))
print(sorted(li))
li.sort()
print(li)

nll = [1, 2, 3, 4, 5, 1]
nll.sort()
print(nll[::-1])
print(nll)

print(list(range(1,100)))

dil = ' '
ndl = dil.join(['hi', 'why', 'die', 'sigh'])
print(ndl)

a,b,c,*o,d,e = 1,2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)
print(o)
print(d)
print(e)