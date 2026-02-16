class user:
    def sign_in(self, username, password):
        self.username = username
        self.password= password

        if username == 'username' and password == 'password':
            print('Run this block')

        else:
            print('credential error')

    def run(self):
        print(f'Well the username is {self.username} and the password is {self.password}')

    def errorcheck(self):
        print(f'check if this print out')

si = user()
si.sign_in('username', '123')
si.run()
si.errorcheck()