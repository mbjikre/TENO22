#lambda expression
#map, filter, reduce, zip
from functools import reduce

li = [1,2,3,4,5]
si = [6,7,8,9,10]
def sqr(i):
    return i*i

def odd(i):
    return i % 2 != 0

def axe(acc, i):
    print(acc, i)
    return acc + i

print(list(map(sqr, li)))
print(list(map(lambda i: i*i, li)))

print(list(filter(odd, li)))
print(list(filter(lambda i: i %2 != 0, li)))

print(list(zip(li, si)))

print(reduce(axe, li, 0))
print(reduce(lambda acc, i: acc+i, li))

print(li)

#square
fi = [5,4,3]
print(list(map(lambda i: i*i, fi)))

#List sorting
sl = [(0,2), (4,3), (9,9), (10,-1)]
sl.sort(key=lambda i:i[1])
print(sl)