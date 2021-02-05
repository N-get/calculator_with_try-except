
def add(a, b):
    try:
        return a + b
    except:
        return "Error"

def subtract(a, b):
    try:
        return a - b
    except:
        return "Error"
def multiply(a, b):
    try:
        return a * b
    except:
        return "Error"

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Divide by zero not possible.")
    except:
        return "Error"

print("Pick your operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    user_input = input("Enter your choice:  ")
    a = float(input("Enter your first number:   "))
    b = float(input("Enter your second number:  "))

    if user_input == '1':
        print(add(a, b))
    elif user_input == '2':
        print(subtract(a,b))
    elif user_input == '3':
        print(multiply(a,b))
    elif user_input == '4':
        print(divide(a, b))
    else:
        print("Invalid input!")
    