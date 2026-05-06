print("Calculator Project") #Initial code....
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Available operations: Addition, Subtraction, Multiplication, Division")
ch = input("What operation do you want?: ").lower()

# Using .lower() simplifies the logic
if ch == "addition":
    print(f"Result: {num1 + num2}")

elif ch == "subtraction":
    print(f"Result: {num1 - num2}")

elif ch == "multiplication":
    print(f"Result: {num1 * num2}")

elif ch == "division":
    # Checking for division by zero to prevent crashes
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Try Again. Invalid choice.") 
