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