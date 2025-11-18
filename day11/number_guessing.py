import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():

    while True:
        level = input("Choose difficulty (easy/hard): ").lower().strip()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("\nInvalid input. Please type 'easy' or 'hard'.")

def check_answer(guess, answer, turns):

    if guess < answer:
        print("Too low.")
        return turns - 1
    elif guess > answer:
        print("Too high.")
        return turns - 1
    else:
        print(f"\nYou got it! The answer was {answer}.")
        return 0

def play_one_round():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while turns > 0:
        print(f"\nYou have {turns} attempt(s) remaining.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not (1 <= guess <= 100):
            print("Please guess a number between 1 and 100.")
            continue

        turns = check_answer(guess, answer, turns)

        if turns == 0 and guess != answer:
            print(f"\nYou've run out of guesses. The number was {answer}. Better luck next time!")

        if guess != answer and turns > 0:
            print("Guess again.\n")

def main():

    print(logo + "\n")

    while True:
        play_one_round()

        print("\n" + "—" * 40)

        while True:
            again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if again in ["yes", "y"]:
                print("\nGreat! Starting a new game...\n")
                break
            elif again in ["no", "n"]:
                print("\nThanks for playing! See you next time! 👋")
                return
            else:
                print("Please type 'yes' or 'no'.")

main()