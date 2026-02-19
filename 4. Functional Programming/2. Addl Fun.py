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
print(list(filter(odd, li)))
print(list(zip(li, si)))
print(reduce(axe, li, 0))
print(li)
