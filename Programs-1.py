class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == '+':
            return self.a + self.b
        elif operation == '-':
            return self.a - self.b
        elif operation == '*':
            return self.a * self.b
        elif operation == '/':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation."
a = float(input("Enter a number: "))
b = float(input("Enter b number: "))
operation = input("Enter an operation (+, -, *, /): ")
calc = Calculator(a, b)


result = calc.calculate(operation)
print(result)
