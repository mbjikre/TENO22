username = input('Please provide username: ')
password = input('Please provide password: ')

len_pass = len(password)
secret = '*' * len_pass
print(f'Hey {username}, your password is :{secret} and it is {len(password)} characters long.')