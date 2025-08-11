def simple_calculator():
    print("Simple Calculator")
    print("Operations: + (addition), - (subtraction), * (multiplication), / (division)")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operation!")
            return
            
        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    simple_calculator()