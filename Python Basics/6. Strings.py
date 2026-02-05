print('Enter your username and password\n')
username = 'username'
password = 'password'

chku = input()
chkp = input()

if username == chku:
    if password == chkp:
        print('Correct details')
else:
    print('Try again')

long_string='''
WOW
O O
===
'''

print(long_string)

combined = username + ' & ' + password
print(combined)

a = 'henlo'
b = str('5')
print(a + ' ' + b)
print(type(int(str(5))))

weather = "It\'s \t\"kind of\"\t sunny \nHave a good day"
print(weather)