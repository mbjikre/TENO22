picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for i in picture:
    for p in i:
        if p == 1:
            print('^', end='')
        else:
            print(' ', end='')
    print('')

while True:
    l = input()
    if l == 'exit':
        break
i = 0
while i < 50:
    i += 1
    print(i)

ini = int(input('Choose one the options:\n1. Multiplication\n2. Division\n3. Addition\n4. Substraction :-'))
while ini <= 5:
    if ini == 1:
        a = int(input())
        b = int(input())
        print(f'Result is {a*b}')
        break

f=0
while f < len([1,2,3,4,5]):
   print('hi')
   f += 1