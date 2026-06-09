# Project 08 — PIG Dice Game

## What it does
A multiplayer terminal dice game for 2 to 4 players. On each turn a player
rolls repeatedly to accumulate points — but if they roll a 1 they lose all
points earned that turn. They choose when to bank their points and pass to
the next player. First to reach 50 points wins.

## What I learned
- How to use a nested loop — an outer `while` loop for the game and an
  inner `for` loop cycling through players each round
- How to use a list to track scores for multiple players dynamically —
  `[0] * num_players` creates a list of zeros sized to the player count
- How to use a boolean flag (`winner_found`) to break out of an outer
  loop from inside an inner loop
- How to use `random.randrange(1, 7)` to simulate a fair six-sided die —
  `randrange` excludes the upper bound so 7 is never rolled
- How to implement a risk/reward mechanic in code — the player decides
  when to stop, and a roll of 1 punishes greed
- How to track both a turn score and a total score separately and only
  merge them when the player banks safely

## What was hard
- Breaking out of the outer `while` loop when a winner is found inside
  the inner `for` loop — using a `winner_found` flag and a `break` after
  setting it was the cleanest solution
- Making sure the turn score reset to 0 correctly on a roll of 1 without
  affecting the total score already banked

## What I would add next
- A configurable target score so players can choose a longer or shorter game
- A computer player with a simple strategy — roll until turn score
  reaches 20 then bank
- A score history showing each player's score after every round
- Coloured output using `colorama` to make each player's turn visually distinct
- A rematch option at the end without restarting the program
