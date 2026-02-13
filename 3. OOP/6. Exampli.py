class first():
    assump = []
    def __init__(self, fn1):
        self.fn1 = fn1
        
    def caller(self):
        for call in self.fn1:
            return print('caller output')
    
class second():
    def __init__(self, fn2):
        self.fn2 = fn2

        def fn2():
            return f'This is second function {self.fn1}'
        
class third():
    def __init__(self, fn3):
        self.fn3 = fn3
        
        def fn3():
            return f'This is third function {self.fn1}'
    
ass = []
ex2 = second('2nd')
ex3 = third('3rd')

ass.append(ex2)
ass.append(ex3)
print(ass)

as2 = first(ass)
as2.caller()