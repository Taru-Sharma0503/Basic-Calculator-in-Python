def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a/b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operator=input("Enter operator (+, -, *, /): ")
match operator:
    case '+':
        print(f"Result = {add(a,b)}")
    case '-':
        print(f"Result = {subtract(a,b)}")
    case '*':
        print(f"Result = {multiply(a,b)}")
    case '/':
        try:
            print(f"Result = {divide(a,b)}")
        except ValueError as e:
            print(e)