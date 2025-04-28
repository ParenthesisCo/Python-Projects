import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True


while running:
    while player not in options:
            player = input("Enter a choice (rock, paper, scissors):   ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose!")

play_again = input("Play again (y/n):  ").lower()
if play_again == "y":
    running = True
elif play_again == "n":
    running = False
else:
    print("Enter a valid option")
