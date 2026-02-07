user = {
    'k1' : 'v1',
    'k2' : 'v2',
    'k3' : 'v3'
}

for a,c in user.items():
    print(a,c)

for k in user.keys():
    print(k)

for v in user.values():
    print(v)

for i in user:
    print(i)

print(type(user.keys()))

lst = [1,2,3,4,5,6,7,8,9]
c = 0
for i in lst:
    c += i

print(c)

for a in range(1,5):
    print(list(range(1,5)))

for _,char in enumerate(range(10,0,-1)):
    print(_,char)
