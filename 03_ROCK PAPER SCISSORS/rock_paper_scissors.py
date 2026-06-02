import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type: ROCK / PAPER / SCISSORS or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please type rock, paper, or scissors.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("")
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        draws += 1
        print("It's a draw!")

    elif user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("You won!")

    elif user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("You won!")

    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You won!")

    else:
        computer_wins += 1
        print("You lost!")

print("")
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Draws:", draws)
print("")

if user_wins > computer_wins:
    print("You are the WINNER!")
elif computer_wins > user_wins:
    print("You LOST!")
else:
    print("It's a tie overall!")

print("Goodbye!")