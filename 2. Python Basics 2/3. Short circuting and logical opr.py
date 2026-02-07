# <
# <=
# >
# >=
# ==
# !=

a = True
b = True

if a and b:
    print('both conditions match')

if a or b:
    print('condition don\'t match')

a = 0
b = 0
print(a == b)


is_m = False
is_e = False

if is_m and is_e:
    print('You are a master magician')
elif is_m and not is_e:
    print('Atleast you\'re getting there')
elif not is_m:
    print('You need magic powers')
else:
    print('you sir are a total loser')


print(bool(''))
print(True == 1)
print('1' == 1)
print([1] == 1)

ind = (1,2,3,4,5)
print(1 == ind[0])