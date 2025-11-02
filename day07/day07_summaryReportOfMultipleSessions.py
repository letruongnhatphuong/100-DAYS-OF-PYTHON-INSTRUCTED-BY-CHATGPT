'''🎯 Goal

Write a Python program that:

Keeps collecting lists of numbers from the user (just like Day 6).

After each round, calculates:

average

maximum

minimum

Stores each result in a summary list.

When the user quits, prints a summary table of all sessions.
'''

def find_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

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
    summaries = []

    while is_running:
        try:
            raw_nums = input("Enter numbers separated by spaces: ").strip()

            # Check for blank input
            if len(raw_nums) == 0:
                print("Please enter something!")
                continue

            # Convert all to float
            converted = [float(n) for n in raw_nums.split()]

            avg = find_average(converted)
            maximum = find_maximum(converted)
            minimum = find_minimum(converted)

            print(f"Average: {avg:.2f}")
            print(f"Maximum: {maximum:.2f}")
            print(f"Minimum: {minimum:.2f}")

            summaries.append((avg, maximum, minimum))

        except ValueError:
            print("Please enter valid numbers only!")
            continue

        # Ask if user wants to continue
        choice = ask_yes_no("Do you want to play again? (y/n): ")
        if choice == "n":
            is_running = False

    # Print summary after exit
    if summaries:
        print("\n📊 Session Summary:")
        print("---------------------------------")
        print("Round | Average |  Max |  Min")
        print("---------------------------------")
        for i, (avg, maximum, minimum) in enumerate(summaries, start=1):
            print(f"{i:>5} | {avg:>7.2f} | {maximum:>5.2f} | {minimum:>5.2f}")
        print("---------------------------------")

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
