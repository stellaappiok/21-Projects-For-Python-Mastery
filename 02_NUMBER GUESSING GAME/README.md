# Project 02 — Number Guessing Game

## What it does

A terminal game where the user sets a number range, a random number is generated within it, and the player guesses until they get it right. The game counts how many guesses it takes.

## What I learned

- How to use the `random` module to generate random numbers
- How to validate user input using `.isdigit()` before converting to an integer
- How to use a `while True` loop with a `break` condition
- How to give directional hints — above or below — to guide the player

## What was hard

- Understanding when to use `break` vs `continue` inside a while loop
- Handling invalid input gracefully without crashing the program

## What I would add next

- A difficulty setting that limits the number of guesses allowed
- A replay option at the end without restarting the program
- Tracking the best score across multiple rounds
