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