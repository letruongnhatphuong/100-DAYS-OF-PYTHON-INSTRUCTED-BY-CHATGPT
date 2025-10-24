'''
🎯 Goal

Write a Python program that:
	1.	Asks the user for a list of numbers (entered in one line, separated by spaces).
	2.	Converts them into integers.
	3.	Separates them into even and odd numbers.
	4.	Displays both lists clearly.
'''

def numberAnalyzer():

    try:
        numInput = input("Please enter a list of numbers in one line, " \
        "seperated by spaces: ").split()
        evenNum = []
        oddNum = []
        for num in numInput:
            num = int(num)
            if num % 2 == 0 :
                evenNum.append(num)
            else:
                oddNum.append(num)

        print("Even numbers are: ", ", ".join(str(n) for n in evenNum))
        print("Odd numbers are: ", ", ".join(str(n) for n in oddNum))

    except ValueError:
        print("Please enter valid values!")

numberAnalyzer()