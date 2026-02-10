# Methods vs Function
def doc(string):
    '''
    Simple docstring

    just as print
    '''
    print(string)
    return string

doc(':::')
print(doc.__doc__)

def sup(*args, **kwargs):
    t = 0
    for i in kwargs.values():
        t = t+i
    return sum(args) + t

print(sup(1,2,3,4,5, num1=5, num2=10))

def hie(lis):
    li = []
    for i in lis:
        if not i % 2 and i not in li:
            li.append(i)
    return max(li)
print(hie([10,2,3,4,8,11]))

def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))