print("Welcome to Quiz School !")

play = input("Do you want to play this quiz (Yes/No)? - ").capitalize()

Score = 0

if play == "Yes":
    print("Okay, let's play !")

    print("")
    q1 = input("What does CPU stand for? - ").lower()

    if q1 == "central processing unit":
        Score += 1
        print("Correct!")
        print(f"Score = {Score}")

    else:
        print("Wrong! Correct Answer - central processing unit ")
        print(f"Score = {Score}")

    print("")
    q2 = input("What does ROM stand for? - ").lower()

    if q2 == "read-only memory":
        Score += 1
        print("Correct!")
        print(f"Score = {Score}")

    else:
        print("Wrong! Correct Answer - read-only memory ")
        print(f"Score = {Score}")

    print("")
    q3 = input("What does RAM stand for? - ").lower()

    if q3 == "random access memory":
        Score += 1
        print("Correct!")
        print(f"Score = {Score}")

    else:
        print("Wrong! Correct Answer - random access memory ")
        print(f"Score = {Score}")

    print("")
    q4 = input("What does GPU stand for? - ").lower()

    if q1 == "graphics processing unit":
        Score += 1
        print("Correct!")
        print(f"Score = {Score}")

    else:
        print("Wrong! Correct Answer - graphics processing unit ")
        print(f"Score = {Score}")

    print("")
    q5 = input("What does PSU stand for? - ").lower()

    if q5 == "power supply unit":
        Score += 1
        print("Correct!")
        print(f"Score = {Score}")

    else:
        print("Wrong! Correct Answer - power supply unit ")
        print(f"Score = {Score}")

else:
    print("Thank You!")
    quit

percentage = Score / 5 * 100

print (f"Your final score was {Score}/5, that is {percentage}%")
