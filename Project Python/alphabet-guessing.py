import string
import random
import time

running = True
str = string.ascii_lowercase
guess_random = random.choice(str)

while running:
    guess = input("Guess the letter of the alphabet i have chosen:  ").lower()
    gs = 0
    
    if guess != guess_random:
            print("Guess again")
            gs += 1
    elif guess == guess_random:
            print(f"{guess} was correct!")
            time.sleep(2)
            print(f"You guessed {gs} times")
            break
# Made by ~tobi_adabs
