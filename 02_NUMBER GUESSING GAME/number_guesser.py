import random
number = input("Enter an number to set the range? ")

if number.isdigit():
    number = int(number)

    if number <= 0:
        print("Please, type a number greater than 0, next time.")
        quit()

else:
    print("Please,enter a number next time.")
    quit()


random_number = random.randrange(0, number)
guesses = 0

while True:
    guesses += 1
    print("")
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please,enter a number next time.")
        continue

    if user_guess == random_number:
        print(f"You got it CORRECT!")
        print(f"You guessed {guesses} times!")
        break

    elif user_guess > random_number:
        print(f"Your guess was above the number.")

    else:
        print(f"Your guess was below the number.")
        print()
