'''🎯 Goal

Write a Python program that:
	1.	Asks the user for a list of numbers (in one line, separated by spaces).
	2.	Converts them to integers.
	3.	Finds and prints the largest and smallest number in that list.'''

def main():

	while True:
		try:
			numbers = input("Please enter a list of numbers seperated by spaces (q to quit): ").split()
			
			if numbers[0].lower() == "q":
				print("Good bye!")
				break

			numbers = [int(num) for num in numbers]

			print(f"The largest number is: {max(numbers)}")
			print(f"The smallest number is: {min(numbers)}")
				
		except ValueError:
			print("Please enter numbers only!")

main()