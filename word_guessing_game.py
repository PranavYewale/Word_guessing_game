import random
import numpy as np


words = np.array(["hello", "fibre", "table", "error", "solve", "space",
                  "video", "power", "chess", "guess", "boron", "study",
                  "spilt", "month", "array", "basis", "basic", "anger",
                  "beach", "award", "alert", "knife", "level", "dream", "claim"])

word_to_be_guessed = random.choice(words)
print("*******************| Welcome to 5 letter Word Guessing Game |*******************")

chances = 5
wrong_guesses = 0
while (chances != 0):
    print()
    user_guess = (input("Enter a word: ")).lower()
    print()

    # Create a list of characters in the word to be guessed
    char_list = list(word_to_be_guessed)

    # Create a list of characters in the user's guess
    guess_list = list(user_guess)

    # Iterate over the characters in the word to be guessed
    try:
        if len(user_guess) > 5:
            print("❕ The word should be of Five letters")

        if user_guess == "quit":
            break

    except:
        pass

    try:

        for i, char in enumerate(char_list):
            # If the character is in the word_to_be_guessed, print a message
            if char in guess_list:
                print(f"['{char}'] is in the word")
                # If the character is in the right place in the user's guess, print a message
                try:
                    if guess_list.index(char) == i:
                        print(f"❁ {char} is in the right place")
                except ValueError:
                    # If the character is not in the user's guess, do nothing
                    pass

    except:
        pass

    try:
        print(f"""
    ['{user_guess[0]}']['{user_guess[1]}']['{user_guess[2]}']['{user_guess[3]}']['{user_guess[4]}']""")

    except:

        pass

    chances -= 1
    print()
    print(f"You have {chances} chances left")

    if user_guess == word_to_be_guessed:
        print("Congrats thats a right word")
        break

    if chances == 0:
        print("Game Over")

        ask = (input("Do you want to continue with Extra 3 chances ")).lower()
        if ask == "y":
            chances += 3
            continue

        elif ask == "n":
            print(f"The Correct Word was: {word_to_be_guessed}")
            break
        else:
            print("sry that was an invalid input")
