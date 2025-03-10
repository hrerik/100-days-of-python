new_calc = True # Will use 'result' for 'num1' if False, otherwise the user will give the value

# Lists for validations
operations = ["+","-","*","/"]
calc_options = ["y","n","t"]

result = 0.0

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 != 0.0:
        return n1 / n2
    else:
        print("Can't divide by zero. 0 will be used.")
        return 0.0

def call_ops(n1, n2, operation):
    """Calls the calculation functions depending on the given operator and returns the result"""
    num = 0
    if operation == "+":
        num = add(n1, n2)
    elif operation == "-":
        num = subtract(n1, n2)
    elif operation == "*":
        num = multiply(n1, n2)
    elif operation == "/":
        num = divide(n1, n2)
    else:
        print("Invalid operation")

    return num

# Algorithm execution
while True: # Will repeat until 'break' (at the end, check 'opt' variable)

    # Gathering input
    if new_calc:
        num1 = float(input("What will be the first number?\n>"))
    else:
        num1 = result
    op = input('What will be the operation? ("+"|"-"|"*"|"/")\n>')
    while op not in operations:
        op = input("Invalid operation selected.\n>")
    num2 = float(input("What will be the second number?\n>"))
    while op == "/" and num2 == 0.0:
        num2 = float(input('When dividing the divider can\'t be zero.\n>'))

    result = call_ops(num1,num2,op) # Call function that return calculation result

    # Printing results and asking for instructions
    print(f"Result: {result}")
    print("Would you like to:")
    print('1. Continue using this number ("y")')
    print('2. Start a new calculation ("n")')
    opt = input('3. Terminate calculator ("t")\n>')
    while opt not in calc_options:
        opt = input("Invalid response.\n>")

    # Checking which instruction to follow
    if opt == "t":
        break
    elif opt == "n":
        new_calc = True
    elif opt == "y":
        new_calc = False
