name = input("Enter your name: ")
print("Welcome", name, "to this adventure")
print("")

answer = input("You are on a dirt way and the road has come to an end, you can go left or right?"
               "Which way would you like to go? ").lower()

if answer == "left":
    print("")
    answer = input("You ahve coem to a river, you can walk around it or swim across."
                   "Which would you do? swim or walk: ")

    if answer == "swim":
        print("")
        print("You swam across and were eaten by an alligator!")

    elif answer == "walk":
        print("")
        print("You walked for many miles and ran out of water and died.")

    else:
        print("")
        print("Not a valid answer")
        print("You LOSS!")


elif answer == "right":
    print("")
    answer = input(
        "You come to a bridge and it looks wobbly, will you cross , go back or swim across? (cross / swim / back): ").lower()

    if answer == "swim":
        print("")
        print("You get back to the river and is attacked by an alligator.")
        print("You died.")

    elif answer == "cross":
        print("")
        answer = input(
            "You cross the bridge and meet a stranger, will you talk to them, (Yes/No)? ")

        if answer == "yes":
            print("")
            print("The strnager helps you find your way back home.")
            print("You have WON the game.")

        elif answer == "no":
            print("")
            print("You continue to wonder around and ran out of resources and died.")
            print("YouLOST this game!")

        else:
            print("")
            print("Not a valid answer")
            print("You LOSS!")

    elif answer == "back":
        print("")
        print("You go back and loss")

    else:
        print("")
        print("Not a valid answer")
        print("You LOSS!")

else:
    print("")
    print("Not a valid answer")
    print("You LOSS!")
