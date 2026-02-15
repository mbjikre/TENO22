class Calculator:
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b


class CalculatorApp:
    
    def __init__(self, calculator):
        self.calculator = calculator   # store the calculator object

    def run(self):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation == "+":
            result = self.calculator.add(num1, num2)
        elif operation == "-":
            result = self.calculator.subtract(num1, num2)
        elif operation == "*":
            result = self.calculator.multiply(num1, num2)
        elif operation == "/":
            result = self.calculator.divide(num1, num2)
        else:
            print("Invalid operation")
            return
        
        print("Result:", result)


# Create objects
my_calculator = Calculator()
app = CalculatorApp(my_calculator)

# Run the app
app.run()
