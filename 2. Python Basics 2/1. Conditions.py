a = True
b = True

if a:
    print(f'is {True}')
elif b:
    print(f'is also {True}')

else:
    print(f'is {False}')

Fin = int(input('Please chose one : \n1. Multiplication\n2. Division\n3. Addition\n4. Substraction\n'))

if Fin == 1:
    a = int(input('Enter two numbers :\n'))
    b = int(input(''))
    print(f'\nMultiplication of the numbers is : {a*b}')

elif Fin == 2:
    a = int(input('Enter two numbers :\n'))
    b = int(input(''))
    print(f'\Division of the numbers is : {a/b}')
elif Fin == 3:
    a = int(input('Enter two numbers :\n'))
    b = int(input(''))
    print(f'\Addition of the numbers is : {a+b}')
elif Fin == 4:
    a = int(input('Enter two numbers :\n'))
    b = int(input(''))
    print(f'\Substraction of the numbers is : {a-b}')

else:
    print('Wrong input')