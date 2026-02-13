class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
    
    def __str__(self):
        return f'{self.color}'
    
    def __format__(self):
        return 10
    
    def __len__(self):
        return 15
    
class Boy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

dre = Boy('first', 2021)
print(dre.color)

axc = Toy('cyka', 'blyat')
print(axc.age)
print(axc.__str__())
print(str(axc))
print(axc.__format__())
print(len(axc))
print(axc.__len__())

class Roy(Toy):
    def __init__(self, color, age):
        super().__init__(color, age)

axe = Roy('What', 'the')
print(axe.age)