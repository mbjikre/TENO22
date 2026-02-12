class user:
    def __init__(self, name, age, work, status):
        self.name = input('Enter username: ')
        self.age = input('Enter age: ')
        self.work = input('Enter work: ')
    
    def work(self):
        pass

user1 = user(1, 2, 3, 4)
user2 = user(1, 2, 3, 4)


print(user1.name, user1.age, user1.work)
print(user2.name, user2.age, user2.work)

