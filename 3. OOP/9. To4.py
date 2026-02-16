class user:
    def sign_in(self, username, password):
        self.username = username
        self.password= password

        if username == 'username' and password == 'password':
            print('Run this block')

        else:
            print('credential error')

si = user()
si.sign_in('username', '123')
