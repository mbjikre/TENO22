class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
cat1 = Cat('Abc', '12')
cat2 = Cat('Def', '23')
cat3 = Cat('Ghi', '34')

def olc(*agrs):
    return max(agrs)

print(f'Oldest cat is {olc(cat1.age, cat2.age, cat3.age)} years old')

el = []
el.append(cat1.age)
el.append(cat2.age)
el.append(cat3.age)
print(el)

print(max(el))

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is {self.age} years old, just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Addon(Cat):
    def run(self, sounds):
        return f'{sounds}'

my_cats = []
cat1 = Simon('Simon', 10)
cat2 = Sally('Sally', 15)
cat3 = Addon('Addon', 5)

my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)
print(my_cats)

my_pets = Pets(my_cats)

my_pets.walk()

for char in [cat1, cat2, cat3]:
    char.walk()
    print(char)

print(issubclass(Cat, Pets))