# Project 21 — Shortest Path Finder (BFS Maze Solver)

## What it does

A visual maze solver that uses Breadth-First Search (BFS) to find the
shortest path from start (S) to end (E) through a hardcoded grid maze.
The algorithm animates in real time using `curses` — walls appear in cyan
and the discovered path trails in yellow, updating every 0.15 seconds so
you can watch BFS explore the maze step by step until it finds the exit.

## What I learned

- How to implement Breadth-First Search (BFS) using a `deque` from the
  `collections` module — deque is used instead of a list because
  `popleft()` on a deque is O(1) while `pop(0)` on a list is O(n)
- How BFS guarantees the shortest path — it explores nodes level by level
  (all nodes 1 step away, then 2 steps, then 3...) so the first time it
  reaches the exit it has found the minimum number of steps
- How to represent a maze as a 2D list and navigate it by checking
  adjacent cells in four directions (up, down, left, right)
- How to use an `explored` set to track visited cells and prevent the
  algorithm from revisiting the same position infinitely
- How to carry the full path alongside each position in the BFS frontier
  by storing `(current_position, trail_so_far)` as a tuple — so when
  the exit is found, the complete path is immediately available
- How to animate an algorithm in real time using `curses` —
  `screen.clear()`, `draw()`, and `screen.refresh()` on each BFS step
  creates the live visual effect
- How to use `curses.color_pair()` to display different elements in
  different colours without external libraries

## What was hard

- Understanding why BFS uses a queue (FIFO) not a stack (LIFO) — using
  a stack would turn it into Depth-First Search which does not guarantee
  the shortest path
- Getting the path tracking right — storing the trail as a list inside
  the frontier tuple means each frontier entry carries its own full
  history, which uses more memory but makes path reconstruction instant
- Understanding that `explored` must be updated when a node is added to
  the frontier, not when it is popped — adding it at pop time allows
  duplicate entries into the queue and slows everything down

## What I would add next

- Let the user choose a maze from multiple hardcoded grids or generate
  a random maze using recursive backtracking
- Compare BFS against Depth-First Search visually — run both and show
  the difference in paths explored and steps taken
- Add Dijkstra's algorithm or A\* with weighted cells to compare against
  BFS on non-uniform cost grids
- Let the user move S and E interactively before running the solver
