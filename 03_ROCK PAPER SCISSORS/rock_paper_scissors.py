import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type: ROCK / PAPER / SCISSORS or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock = 0
    # paper = 1
    # scissors = 2
    computer_pick = options[random_number]
    print("")
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("You won!")
        continue

    elif user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("You won!")
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You won!")
        continue

    else:
        computer_wins += 1
        print("You lost!")

print("")
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("")

if user_wins > computer_wins:
    print("You are the WINNER!")

else:
    print("You LOST!")

print(f"Goodbye!")
