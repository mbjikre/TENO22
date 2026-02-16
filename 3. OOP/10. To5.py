class calc:
    def add(self, i1, i2):
        self.i1 = i1
        self.i2 = i2

class adds:
    def add(self, i1, i2):
        return i1 + i2
    
addi = calc()
addi.add(5,10)
print(addi)
