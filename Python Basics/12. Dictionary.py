dictionary = {
    'a' : [1, 2, 3],
    'b' : 'heellloooo',
    'c' : False
}

print(type(dictionary))

dictionary = {
    123 : [1, 2, 3],
    True : 'heellloooo',
    23 : False
}

print(dictionary[True])

user = {
    'name' : 'Jojo',
    'gen' : 'male',
    'age' : 22
}

print(user.get('age', 55))
print(22 in user.values())

user1 = dict(abc = '123')
print(type(user1))

tup = (1,2,3,4,5)
print(5 in tup)