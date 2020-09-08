a = float(input())
b = float(input())

operation = str(input())

def calculator(operation):
    if operation == 'Addition':
        result = a + b
    elif operation == 'Subtraction':
        result = a - b
    elif operation == 'Multiplication':
        result = a * b
    elif operation == 'Division':
        result = a//b
    return result

print(calculator(operation))