# Project 12 — Turtle Racing

## What it does

A visual racing game built with Python's `turtle` module. The user chooses
how many turtles to race (2 to 10). Each turtle is assigned a random colour
and placed at the starting line. They move forward by a random distance each
turn until one crosses the finish line. The winning turtle's colour is
announced in the terminal.

## What I learned

- How to use the `turtle` module to create a graphical window and animate
  objects — `turtle.Turtle()`, `.shape()`, `.color()`, `.forward()`,
  `.setpos()`, `.penup()`, `.pendown()`
- How to set up a screen with specific dimensions using
  `turtle.Screen()` and `.setup()`
- How to use `random.shuffle()` to randomise a list in place, then
  slice it to get exactly the number of colours needed
- How to use `random.randrange()` to move each turtle a random
  distance per frame — creating unpredictable race outcomes
- How to detect when a turtle crosses the finish line by checking
  its y-coordinate against the screen boundary
- How to use `turtles.index(racer)` to look up which colour belongs
  to the winning turtle
- How to use `time.sleep()` to pause the program so the window
  stays open long enough to see the result

## What was hard

- Understanding turtle coordinate system — the origin (0, 0) is the
  centre of the screen, so the bottom left is (-width//2, -height//2)
  not (0, 0) like a normal grid
- Getting the starting positions spaced evenly using integer division
  `width // (len(colors) + 1)` so turtles never overlap

## What I would add next

- Display the winner inside the turtle window itself, not just the terminal
- Show a countdown before the race starts — 3, 2, 1, Go!
- Let the user bet on a turtle before the race and track wins
  across multiple rounds
- Add a race history showing finishing order for all turtles, not
  just the winner
