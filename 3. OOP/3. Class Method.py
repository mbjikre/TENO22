class PC:
    mmship = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def add(cls, num1, num2):
        return num1 + num2
    
    @staticmethod
    def mul(num1, num2):
        return num1*num2
    
print(PC.add(2,3))
print(PC.mul(4,5))

class NameOfClass:
    class_attribue = 'value'
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        #CODE
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        #CODE
        pass

    @staticmethod
    def stc_method(param1, param2):
        #CODE
        pass

print('hello'.upper())