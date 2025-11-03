# Sierra Ceja
# CIS256 EX 4
# Guess the Word

import random

# Creates list of possible words
words = ["pencil", "laptop", "mouse", "notebook", "keyboard"]

# Picks one random words from the list
secret_word = random.choice(words)

# Creates variable to keep track game
guessed_letter = [] # Keeps track of letters guessed by user
attempt_left = 6 # Number of attempts in game
words_guessed = False # Checks if player has guessed word

print("Welcome to the Guess the Word Game!")
print("Try to guess the word one letter at a time.")
print(f"You have {attempt_left} attempts. Good luck!\n")


# Method used to loop game
while attempt_left >0 and not words_guessed:
    # Displays word with underscores for any unguessed letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letter:
            display_word += letter + " "
        else:
                display_word += "_ "
    print("Word:", display_word.strip())

    # Asks the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Checks if the guess is valid
    if len(guess) != 1 or not guess.isalpha(): # Checks string if contain only letters
        print("Please enter one letter only.\n")
        continue
    # Checks if letter has already been guessed
    if guess in guessed_letter:
        print("You already guessed that letter. Try again.\n")
        continue

    # Adds the guessed letter to the list
    guessed_letter.append(guess)

    # Checks if the guess is in the word
    if guess in secret_word:
        print("Good job! The letter is in the word.\n")
    else:
        attempt_left -= 1
        print(f"Sorry, that letter is not in the word. Attempts left: {attempt_left}\n")

    # Checks to see if player has guess all of the letters.
    word_guessed = True
    for letter in secret_word:
        if letter not in guessed_letter:
            word_guess = False
            break
            
# Displays the final result
if word_guessed:
    print(f"Congrats! You guessed the word: {secret_word}")
else:
    print(f"Game over! The word was: {secret_word}")
    
