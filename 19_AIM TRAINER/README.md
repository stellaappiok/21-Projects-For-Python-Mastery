# Project 20 — Aim Trainer

## What it does

A reaction speed game built with `pygame`. Circular targets ("bubbles")
spawn randomly on screen and animate by growing then shrinking. Click them
before they shrink away to score a hit. The game tracks hits, total clicks,
elapsed time, and ends after 3 missed bubbles, displaying final accuracy
and click speed.

## What I learned

- How to build a real-time game loop using `pygame` — handling events,
  updating game state, and redrawing the screen every frame at a
  fixed framerate using `clock.tick(60)`
- How to use object-oriented programming with a `Bubble` class to give
  every target its own position, radius, and growth state, instead of
  managing separate variables for each one
- How to use `pygame.time.set_timer()` combined with a custom event
  (`pygame.USEREVENT + 1`) to spawn new bubbles automatically at a
  fixed interval without blocking the rest of the game
- How to detect a click on a circular object using `math.hypot()` to
  calculate the distance between the mouse position and the bubble's
  centre, then comparing it to the bubble's radius
- How to safely remove items from a list while iterating over it by
  looping over a copy (`bubbles[:]`) instead of the original list
- How to calculate live statistics — speed in targets per second and
  accuracy as a percentage — and update them every frame
- How to build a results screen that waits for user input using its
  own event loop before closing the game

## What was hard

- Understanding why iterating over `bubbles` directly while removing
  items from it causes bugs — modifying a list while looping over it
  skips elements, so looping over `bubbles[:]` (a copy) was necessary
- Getting the bubble click detection right — circular hit detection
  needs distance calculation, not simple rectangle bounds checking
- Coordinating multiple pieces of state every frame — bubble animation,
  click detection, miss counting, and game-over checking all had to
  happen in the right order within a single loop iteration

## What I would add next

- A difficulty setting that increases spawn rate and decreases bubble
  size over time
- A restart option on the results screen instead of requiring the
  game to fully quit
- Sound effects for hits and misses
- A persistent high score saved to a file across sessions
- Smaller bubbles worth more points to reward precision
