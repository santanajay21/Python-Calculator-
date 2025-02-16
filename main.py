from art import logo

"""Below is the calculations of eachh operation in the calculator"""
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def  divide(n1,n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

"""Below is the dictionary of the operations"""
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

"""Below is the calculator function"""
def calculator():
    num1 =  float(input("What's the first number?: "))

    while True:
        opp = input("Pick an operation: +, -, *, /: ")
        if opp not in operations:
            print("Invalid operation")
            continue

        num2 = float(input("What's the next number?: "))
        function = operations[opp]
        result = function(num1, num2)

        print(f"{num1} {opp} {num2} = {result}")

        any_more_operations = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if any_more_operations == 'y':
            num1 = result
        elif any_more_operations == 'n':
                calculator()
        else:
                print("Invalid input")
                break

calculator()