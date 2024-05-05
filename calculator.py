def calculator():
    while True:
        # Get user input
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Perform calculation based on operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Check if num2 is not zero to avoid division by zero error
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero!")
                continue
        else:
            print("Invalid operator!")
            continue

        print("Result:", result)

        # Ask if user wants to continue
        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            break

calculator()
