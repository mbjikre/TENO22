# :=
a = [1,2,3,4,5,6,7,8,9,10,11    ]
if (n := len(a)) > 10:
    print(f'List is too long ({n} elements, expected <= 10)')

price = 100
txt = f'It is {'perfect' if price == 100 else 'ok'}'
print(txt)

while ((n := len(a))) > 1:
    print(f'Lenght is {n} elements long : \n{a}')
    a = a[:-1]
    #print(a)
