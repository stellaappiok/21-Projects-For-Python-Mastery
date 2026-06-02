# Project 03 — Rock Paper Scissors

## What it does
A terminal Rock Paper Scissors game against the computer. The computer
picks randomly each round. The game keeps a running score and continues
until the player types Q to quit, then announces the overall winner.

## What I learned
- How to use `random.randint()` to generate a random choice
- How to use a list to map numbers to string values
- How to use a `while True` loop with a `break` to keep a game running
- How to use `continue` to skip to the next loop iteration cleanly
- How to track score across multiple rounds using counter variables

## What was hard
- Understanding when to use `break` vs `continue` inside the while loop
- Making sure invalid inputs were skipped without crashing the program

## What I would add next
- A best-of-5 or best-of-10 mode
- Show the score after every round, not just at the end
- Track win percentage alongside raw win/loss count