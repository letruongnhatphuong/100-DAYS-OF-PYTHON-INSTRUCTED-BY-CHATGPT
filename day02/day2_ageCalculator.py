'''Write a Python program that:
	1.	Asks the user to enter their name and birth year.
	2.	Calculates their current age automatically.
	3.	Prints a friendly message like:
“Hi Phuong, you are ... years old!”

💡 Use today’s real year (e.g. 2025) in your calculation.'''

from datetime import datetime
def age_calculator():

    current_year = datetime.now().year
    name = input("Please enter your name: ")
    birth_year = int(input("Please enter your birth year: "))
    age = current_year - birth_year
    print(f"Hi {name}, you are {age} years old!")
    
age_calculator()
