# Project 05 — Alarm Clock

## What it does

A terminal countdown alarm. The user enters minutes and seconds to wait,
and the program counts down live in the terminal — updating the display
every second — until it plays a sound when time runs out.

## What I learned

- How to use ANSI escape codes (`\033[2J` and `\033[H`) to clear the
  terminal screen and move the cursor back to the top, creating a
  live-updating countdown effect instead of printing a new line every second
- How to use `time.sleep(1)` inside a loop to create an accurate
  one-second-per-iteration countdown
- How to use the `playsound` library to play an audio file once the
  countdown reaches zero

## What was hard

- Understanding ANSI escape codes — these are special character
  sequences that terminals interpret as commands rather than text,
  which is how the countdown updates in place instead of scrolling
- Getting the minute and second formatting right so the display
  always looks clean regardless of the numbers involved

## What I would add next

- Add a snooze option that restarts the countdown for a few more minutes
- Allow setting an alarm for a specific clock time instead of only
  a countdown duration
- Add a visual progress bar alongside the time display
