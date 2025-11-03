# Sierra Ceja
# CIS256 EX4
# Test Guess the Word

import guess_the_word as game


def test_selected_word_from_list():
    # Checks if the word chosen by the game is in the list of words
    assert game.secret_word in game.words


def test_correct_guess():
    # Checks if a correct letter is recognized
    secret_word = "pencil"
    guessed_letters = []
    result = game.process_guess(secret_word, guessed_letters, "p")

    # result should be a tuple like (True, True, "Correct!")
    is_valid, is_correct, message = result

    assert is_valid == True
    assert is_correct == True
    assert "Correct" in message


def test_incorrect_guess():
    # Checks if an incorrect letter is recognized
    secret_word = "pencil"
    guessed_letters = []
    result = game.process_guess(secret_word, guessed_letters, "z")

    is_valid, is_correct, message = result

    assert is_valid == True
    assert is_correct == False
    assert "Not" in message  # Should say "Not in the word."


def test_repeated_guess():
    # Checks if the game stops you from guessing the same letter again
    secret_word = "laptop"
    guessed_letters = ["l"]
    result = game.process_guess(secret_word, guessed_letters, "l")

    is_valid, is_correct, message = result

    assert is_valid == False
    assert is_correct == False
    assert "already" in message


def test_invalid_input():
    # Check if the game rejects non-letter input like numbers
    secret_word = "mouse"
    guessed_letters = []
    result = game.process_guess(secret_word, guessed_letters, "m")

    is_valid, is_correct, message = result

    assert is_valid == False
    assert is_correct == False
    assert "one letter" in message
