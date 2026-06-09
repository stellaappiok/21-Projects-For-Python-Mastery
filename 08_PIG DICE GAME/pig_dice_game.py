import random

TARGET_SCORE = 50


def throw_dice():
    return random.randrange(1, 7)


def get_player_count():
    while True:
        amount = input("How many players will be playing? (2-4): ")

        if not amount.isdigit():
            print("Please enter a valid number.")
            continue

        amount = int(amount)

        if 2 <= amount <= 4:
            return amount

        print("Number of players must be between 2 and 4.")


num_players = get_player_count()
scores = [0] * num_players

winner_found = False

while not winner_found:
    for player in range(num_players):
        print(f"\n--- Player {player + 1}'s Turn ---")
        print(f"Current Total: {scores[player]}")

        turn_points = 0

        while True:
            choice = input("Roll the dice? (y/n): ").lower()

            if choice != "y":
                break

            dice = throw_dice()
            print(f"You rolled a {dice}")

            if dice == 1:
                print("Oops! You rolled a 1 and lost all points for this turn.")
                turn_points = 0
                break

            turn_points += dice
            print(f"Turn Score: {turn_points}")

        scores[player] += turn_points
        print(f"Total Score: {scores[player]}")

        if scores[player] >= TARGET_SCORE:
            winner_found = True
            winning_player = player
            break

print(
    f"\n🎉 Player {winning_player + 1} wins the game with {scores[winning_player]} points! 🎉"
)