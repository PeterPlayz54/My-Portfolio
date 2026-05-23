print("Welcome to the Python Calculator!")
#Coding the functions for each operation
#addition function
def add(num1, num2):
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")

#subtraction function
def subtract(num1, num2):
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")

#multiplication function
def multiply(num1, num2):
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")

#division function
def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

#power function
def power(num1, num2):
    result = num1 ** num2
    print(f"The result of {num1} ^ {num2} is: {result}")

#square root function
def root(num1, num2):
    if num1 >= 0:
        result1 = round (pow(num1, 1/num2),2)
        print(f"The {num2}th root of {num1} is: {result1}")
    else:
        print("Error: Root of a negative number is not allowed.")

#modulus function
def modulus(num1, num2):
    if num2 != 0:
        print(f"The result of {num1} % {num2} is: {num1 % num2}")
    else:
        print("Error: Modulus by zero is not allowed.")

repeat = True
while repeat:
    print("Operations: 1) Addition, 2) Subtraction, 3) Multiplication, 4) Division, 5) Power, 6) Root, 7) Modulus")
    operation = input("Choose an operation (1-7): ").strip().lower()
    
    #CASE OF statement to determine which operation to perform based on user input
    match operation:
        case "1":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                add(num1, num2)
        case "2":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                subtract(num1, num2)
        case "3":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number(Multiplier): "))
                multiply(num1, num2)
        case "4":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number(Dividend): "))
                divide(num1, num2)
        case "5":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number(Power): "))
                power(num1, num2)
        case "6":
                num1 = float(input("Enter the number: "))
                num2 = float(input("Enter root degree (2 = square root, 3 = cube root): "))
                root(num1, num2)
        case "7":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number(Modulus): "))
                modulus(num1, num2)
        case _:
                print("Invalid operation. Please choose a valid operation from the list.")

    print("Thank you for using this calculator! Would you like to perform another calculation? (yes/no) ")
    ans = input().strip().lower()
    if ans == "yes":
        print("Great! Let's perform another calculation!")
        repeat = True
    else:
        print("No worries! Maybe next time.")
        repeat = False