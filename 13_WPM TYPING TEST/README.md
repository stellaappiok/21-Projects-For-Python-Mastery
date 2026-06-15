# Project 11 — WPM Typing Speed Test

## What it does

A terminal-based typing speed test built with Python's `curses` library.
A random sentence is loaded from a text file and displayed on screen.
As the user types, each character turns green for correct and red for
incorrect in real time. Words per minute is calculated and displayed
live throughout the test. The user can play multiple rounds or exit
with ESC at any time.

## What I learned

- How to use the `curses` library to build interactive terminal UIs —
  controlling the cursor, clearing the screen, and writing to specific
  positions using `addstr(row, col, text)`
- How to use `curses.color_pair()` to display coloured text in the
  terminal — green for correct characters, red for incorrect
- How to use `screen.nodelay(True)` to make key input non-blocking
  so the WPM counter updates continuously without waiting for a keypress
- How to calculate words per minute in real time — dividing characters
  typed by 5 (average word length) then dividing by elapsed minutes
- How to handle backspace across different operating systems by checking
  for `KEY_BACKSPACE`, `\b`, and `\x7f` — three different ways the same
  key is reported depending on the terminal
- How to use `try/except` around `screen.getkey()` to handle the case
  where no key has been pressed yet without crashing
- How to use `curses.wrapper()` to safely initialise and clean up the
  curses environment so the terminal returns to normal after the program exits

## What was hard

- Understanding `nodelay(True)` — without it the WPM counter freezes
  while waiting for the next keypress because `getkey()` blocks by default
- Detecting backspace correctly — different terminals send different
  characters for the same key, so all three variants had to be handled
- Understanding that `curses.wrapper()` handles the setup and teardown
  automatically — without it, a crash leaves the terminal in a broken state

## What I would add next

- A results screen showing final WPM, accuracy percentage, and time taken
- A difficulty selector — Easy (short sentences), Medium, Hard (long passages)
- A high score system that saves your best WPM to a file
- Highlight the current character position with an underscore cursor
  so the user always knows exactly where they are in the sentence
