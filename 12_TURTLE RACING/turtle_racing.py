import turtle
import time
import random

width, height = 500, 500
colors = ["red", "green", "blue", "orange",
          "yellow", "black", "purple", "pink", "brown", "cyan"]


def get_number_of_racers():
    racers = 0

    while True:
        racers = input("Enter the number of racers (2-10): ")

        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try Again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in the range 2-10. Try Again!")


def create_turtles(colors):
    turtles = []
    spacing = width // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-width // 2 + (i + 1) * spacing, -height // 2 + 20)

        racer.pendown()
        turtles.append(racer)

    return turtles


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= height // 2 - 10:
                return colors[turtles.index(racer)]


def init_turtle():
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle Racing!")


racers = get_number_of_racers()
init_turtle()

random.shuffle(colors)
colors = colors[:racers]

winner = race(colors)
print(f"The winner is the {winner} turtle!")

time.sleep(5)
