import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

not_enough = True

while not_enough:
    player = None
    while player not in choices:
        player = input("Rock paper or scissors: ").lower()

    if player == computer:
        print("Computer: " + computer)
        print("Player: " + player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You Lose!")
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You Won!")
    elif player == "paper":
        if computer == "rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You Won!")
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You Lose!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You Lose!")
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You Win!")
    response = input("Want a replay (y/n): ").lower()
    if response != "y":
        break
