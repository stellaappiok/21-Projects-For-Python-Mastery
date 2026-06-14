# Project 15 — NBA Live Scoreboard

## What it does

A terminal app that fetches live NBA scores from ESPN's public API and
displays every game happening today — showing team abbreviations, current
scores, and game status (scheduled, in progress, or final). No API key
required.

## What I learned

- How to use the `requests` library to make a real HTTP GET request
  to a live public API and receive JSON data back
- How to use `.json()` to convert the API response directly into a
  Python dictionary
- How to use `.get()` to safely access dictionary keys without
  crashing if the key does not exist
- How to navigate deeply nested JSON — the data lives inside
  `events → competitions → competitors` which requires chaining
  multiple index accesses to reach the values you need
- How to use a `timeout` parameter in requests to prevent the program
  hanging indefinitely if the API is slow
- How to format and print structured data cleanly in the terminal

## What was hard

- Understanding the structure of the API response — the JSON is deeply
  nested and required careful inspection to find where scores,
  team names, and game status actually live
- Knowing to use `.get("events", [])` instead of `["events"]` so the
  program returns gracefully on days with no games rather than crashing

## What I would add next

- Filter games by a specific team passed as a command line argument
- Add win probability and quarter-by-quarter scoring breakdown
- Colour code scores using `colorama` — red for losing team,
  green for winning team
- Schedule the script to run automatically every 10 minutes
  and print updates using `time.sleep()`
- Add a second sport — NFL or soccer — as a selectable option
