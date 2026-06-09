# Project 09 — Slot Machine

## What it does
A fully functional terminal-based slot machine game. The player deposits
money, chooses how many lines to bet on (up to 3), sets a bet amount per
line, and spins. The machine generates a random 3x3 grid of symbols and
pays out based on matching symbols across each line. The game tracks
balance across multiple spins until the player quits.

## What I learned
- How to build a multi-function program where each function has one
  clear responsibility — deposit, bet, spin, check winnings, print grid
- How to use a dictionary to store symbol frequency and value,
  then build a weighted random pool from it
- How to use `random.choice()` combined with `.remove()` to sample
  without replacement — so the same symbol cannot appear twice in
  one column
- How to use a `for/else` construct — the `else` block on a `for` loop
  runs only if the loop completed without hitting a `break`
- How to structure a game loop that modifies and tracks balance
  across multiple rounds
- How to validate user input robustly using `.isdigit()` and
  range checks inside `while True` loops

## What was hard
- Understanding the `for/else` pattern in `check_winnings` — the `else`
  runs when no `break` occurred, meaning all symbols matched
- Building the weighted symbol pool correctly — looping through
  the dictionary and appending each symbol by its count
- Making sure the total bet check happened before the spin,
  not after

## What I would add next
- Coloured output using `colorama` so winning lines highlight in green
- Sound effects using `playsound` for spin and win moments
- A save system that writes balance to a file so progress persists
  between sessions
- An animation that reveals symbols one by one instead of all at once
- A maximum balance cap and a "you broke the casino" win condition
