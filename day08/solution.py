import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = "_" * word_length
guessed_letters = []
game_over = False

print("Word to guess:", display)

while not game_over:
    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    # Prevent repeat guesses
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again!")
        continue

    guessed_letters.append(guess)
    new_display = ""

    # Reveal guessed letters
    for letter in chosen_word:
        if letter in guessed_letters:
            new_display += letter
        else:
            new_display += "_"

    print("Word to guess:", new_display)

    # Wrong guess → lose life
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

    # Update display
    display = new_display

    # Win condition
    if "_" not in display:
        game_over = True
        print(f"\n🎉 YOU WIN! The word was '{chosen_word}'. 🎉")

    # Lose condition
    elif lives == 0:
        game_over = True
        print(f"\n💀 YOU LOSE! The word was '{chosen_word}'. 💀")

    print(stages[lives])
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))