# Project 13 — Password Generator

## What it does

A terminal-based password generator that creates a random secure password
based on user preferences. The user sets a minimum length and chooses
whether to include numbers and special characters. The generator guarantees
the password always meets the chosen criteria before returning it.

## What I learned

- How to use the `string` module to access built-in character sets
  (`ascii_letters`, `digits`, `punctuation`)
- How to use `random.choice()` to pick random characters from a pool
- How to build a `while` loop that keeps running until multiple conditions
  are all satisfied at the same time
- How to use boolean flags (`has_number`, `has_special`, `meets_criteria`)
  to track whether a requirement has been met
- How to take user input and use it to control program logic

## What was hard

- Understanding the `meets_criteria` logic — making sure both the number
  and special character requirements were checked independently and combined
  correctly using `and`
- Realising that the loop needed to check length AND criteria together,
  not separately

## What I would add next

- Reject inputs other than Yes/No gracefully instead of silently treating
  them as No
- Add a minimum guaranteed count — e.g. at least 2 numbers and 2 special
  characters, not just 1
- Let the user generate multiple passwords in one session
- Add a strength indicator (Weak / Medium / Strong) based on length and
  character variety
