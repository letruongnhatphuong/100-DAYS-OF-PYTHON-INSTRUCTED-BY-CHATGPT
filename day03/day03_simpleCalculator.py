'''🧩 Requirements
	1.	Ask the user for two numbers.
	2.	Ask which operation to perform: +, -, *, or /.
	3.	Perform the operation and print the result.
	4.	Handle division by zero safely.
	5.	If the user enters an invalid operator, print a clear error message.
'''
def calculator():

    running = True
    while running: 
        try:
            num1 = float(input("Please enter first number: "))
            num2 = float(input("Please enter second number: "))
            operation = input("Choose operation (+, -, *, /): ")

            if operation == "+":
                print(f"{num1} + {num2} = ", num1 + num2)
            elif operation == "-":
                print(f"{num1} - {num2} = ", num1 - num2)   
            elif operation == "*":
                print(f"{num1} * {num2} = ", num1 * num2)   
            elif operation == "/":
                print(f"{num1} / {num2} = ", num1 / num2)

        except ZeroDivisionError:
            print("Cannot devide by zero. Try again!")
        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")

        if input("Do you want to perform another calculation? (y/n): ").lower() != 'y':
            running = False

calculator()