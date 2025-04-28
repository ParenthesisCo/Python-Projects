import string
import random

str = string.octdigits
guess_random = random.choice(str)
running = True
guesses = 0

while running:
        guess = input("Guess a number between 1 and 6:  ").lower()
        if guess != guess_random:
            print("That is wrong!")
            print("Try again")
            running = True
            guesses += 1
        elif guess == guess_random:
            print("That is correct!!!")
            print(f"Number of guesses: {guesses}")
            running = False
# Made by ~tobi_adabs