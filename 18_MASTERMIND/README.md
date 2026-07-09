# Project 19 — Mastermind / 4 Color Match

## What it does

A terminal recreation of the classic Mastermind board game. The computer
generates a secret 4-colour code from 6 possible colours (R, G, B, Y, W, O).
The player has 10 attempts to guess the exact code. After each guess the game
gives two hints — how many colours are in the correct position, and how many
correct colours are in the wrong position. The player wins by finding the
exact code before running out of tries.

## What I learned

- How to use `zip()` to iterate over two lists simultaneously — comparing
  each guessed colour against the real code position by position
- How to use a dictionary (`color_counts`) to track remaining unmatched
  colours, so the incorrect position count does not double-count colours
  that were already matched correctly
- How to use a `for/else` construct on the game loop — the `else` block
  runs only when the loop completes all iterations without hitting a `break`,
  which triggers the "you ran out of tries" message cleanly
- How to use `.upper().split(" ")` to normalise user input — converting
  to uppercase and splitting on spaces so "r g b y" and "R G B Y" both work
- How to use `if __name__ == "__main__"` to make the script importable as
  a module without automatically running the game — good practice for any
  reusable Python file
- How to validate input in two separate stages — first checking length,
  then checking each colour individually using a `for/else` inside the
  input loop

## What was hard

- Getting the hint logic right without double-counting — the two-pass
  approach (first count correct positions, then count incorrect positions
  using remaining counts) was the key insight. Doing it in a single pass
  leads to overcounting
- Understanding why the `for/else` pattern works here — the `else` on
  a `for` loop is one of Python's most unusual features and easy to
  confuse with a regular `if/else`

## What I would add next

- Colour the output using `colorama` so each letter appears in its
  actual colour — R prints red, G prints green, and so on
- Add a difficulty setting that changes code length and number of tries
- Show a history of all previous guesses and their hints after each round
- Add a hint system that reveals one correct colour position on request
  at the cost of an extra try
