a=float(input("Enter a number: "))
b=float(input("Enter b number: "))
operation=input("Enter an operation (+, -, *, /): ")
if operation == '+':
    result = a + b
    print(result)
elif operation == '-':
    result = a - b
    print(result)
elif operation == '*':
    result = a * b
    print(result)
elif operation == '/':
    if b != 0:
        result = a / b
        print(result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")
