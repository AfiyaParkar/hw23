
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("FUNCTION CALCULATOR")

try:
    # Part 2: Ask for numbers and operation
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Operation (add, subtract, multiply, divide): ")

    # Part 3: Compare operation and print the result
    if operation == "add":
        print("Result:", add(num1, num2))
    elif operation == "subtract":
        print("Result:", subtract(num1, num2))
    elif operation == "multiply":
        print("Result:", multiply(num1, num2))
    elif operation == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Unknown operation.")

# Part 4: Handle errors and print the closing message
except ValueError:
    print("Please type numbers only.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("Thanks for using the calculator!")
