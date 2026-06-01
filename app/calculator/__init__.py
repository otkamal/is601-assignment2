from app.operations import addition, subtraction, multiplication, division

def calculator():
    print("Welcome to the calculator REPL. Type 'exit' to quit.")
    while True:
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")
        user_input = user_input.lower()
        if user_input == "exit":
            print("Exiting calculator... Goodbye ~")
            break

        try:
            operation, a, b = user_input.split()
            a, b = float(a), float(b)
        except ValueError as e:
            print("Invalid input. Please follow <operation> <a> <b> syntax.")
            continue

        if operation == "add":
            result = addition(a, b)
        elif operation == "subtract":
            result = subtraction(a, b)
        elif operation == "multiply":
            result = multiplication(a, b)
        elif operation == "divide":
            try:
                result = division(a, b)
            except ZeroDivisionError as e:
                print(e)
                continue
        else:
            print(f"Unknown operation {operation}. Supported operations: add, subtract, multiply, divide.")
            continue

        print(f"Result: {result}")