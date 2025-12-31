# I WILL MAKE A ROCK, PAPER AND SCISSOR GAME.
import random
choices = ["rock", "paper", "scissor"]
user = input("Enter any one (rock, paper, scissor): ").lower()
robot = random.choice(choices)
print("Robot chose:", robot)
if user not in choices:
    print("Error: Maybe spelling mistake or number entered.")
else:
    if user == robot:
        print("Oop's, It's a Draw!")
    elif (user == "rock" and robot == "scissor") or \
         (user == "paper" and robot == "rock") or \
         (user == "scissor" and robot == "paper"):
        print("You Win!")
    else:
        print("Robot Wins!")
