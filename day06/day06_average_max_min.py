'''Goal

Write a Python program that:

Asks the user for a list of numbers (in one line, separated by spaces).

Uses functions to:

find the average

find the maximum

find the minimum

Prints all results clearly.'''

def find_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total/count

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer
        print("Invalid input. Please enter 'y' or 'n'.")

def main():

    is_running = True
    while is_running:
        try:
            raw_nums = input("Enter numbers seperated by spaces: ").strip()

            #Check for blank input
            if len(raw_nums) == 0:
                print("Please enter something!")
                continue
            
            #Convert all to float
            converted = [float(n) for n in raw_nums.split()]

            print(f"Average: {find_average(converted):.2f}")
            print(f"Maximum: {find_maximum(converted):.2f}")
            print(f"Minimum: {find_minimum(converted):.2f}")

        except ValueError:
            print("Please enter valid numbers only!")
            continue
        
            #Ask if use want to continue
        choice = ask_yes_no("Do you want to play again? (y/n): ")
        if choice == "n":
            print("Thank you for playing!")
            is_running = False

if __name__ == "__main__":
    main()




    

