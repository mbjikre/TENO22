class Try:
    def prime():
        pass

    def adds(num1, num2):
        return int(num1) + int(num2)

class Try2:
    def passer(num1, num2):
        return int(num1) + int(num2)


obj1 = Try()

print(type(0))
print(type('a'))
print(type(0.1))
print(type(print))
print(type(float))
print(type(Try.prime))
print(type(obj1))
print(isinstance(ModuleNotFoundError, object))
print(issubclass(Try, object))


ins1 = Try2.passer(5,5)

print(ins1)