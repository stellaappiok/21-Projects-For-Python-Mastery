# Project 08 — Timed Math Challenge

## What it does
A terminal-based timed math quiz that generates random arithmetic problems
using addition, subtraction, and multiplication. The user sets the operand
range and total number of questions. The game tracks how long they take and
how many they get wrong, then gives a performance rating at the end.

## What I learned
- How to use the `time` module to measure elapsed time with
  `time.time()` at the start and end of a session
- How to use `eval()` to compute the result of a dynamically generated
  math expression stored as a string
- How to use `random.randint()` and `random.choice()` to generate
  random numbers and operators
- How to use a `while True` loop inside a `for` loop to keep asking
  the same question until the user gets it right
- How to use `round()` to clean up floating point time values
- How to chain `if/elif` conditions to give tiered performance feedback

## What was hard
- Understanding that `eval()` takes a string like `"3 + 7"` and
  actually computes it — powerful but needs careful use since eval
  will execute any Python code passed to it
- Making sure the wrong counter incremented correctly — it counts
  every failed attempt, not just every failed question

## Bug fixed
- Removed unused `from pyparsing import printables` — this import
  was not needed and would cause an error if pyparsing is not installed

## What I would add next
- A division operator with whole number answers only to avoid decimals
- A difficulty selector — Easy, Medium, Hard — that sets operand
  ranges automatically
- A leaderboard that saves the top 5 fastest times to a file
- A per-question time limit so the game has more pressure
