# Project 09 — Madlibs Generator

## What it does

A terminal Madlibs game that reads a story from a text file containing
placeholders like `<noun>`, `<verb>`, and `<adjective>`. It finds every
unique placeholder, asks the user to fill each one in, then prints the
completed story with all placeholders replaced by the user's words.

## What I learned

- How to read a text file using `open()` with a context manager (`with`)
  so the file closes automatically after reading
- How to parse a string character by character using a `for` loop —
  tracking state with a boolean flag (`inside_placeholder`) to know
  when you are inside `< >` brackets
- How to build a word incrementally by appending characters to a string
  variable as you loop through them
- How to use a list to collect unique placeholders — checking `if
current_word not in placeholders` before appending to avoid duplicates
- How to use a dictionary to map each placeholder to its replacement word
- How to use `str.replace()` to substitute all occurrences of a
  placeholder in a string in one line

## What was hard

- Understanding the state machine logic — using `inside_placeholder`
  as a flag to switch between two modes: reading normal text and
  reading a placeholder
- Making sure the `<` and `>` characters were included in the
  placeholder string so `replace()` could find exact matches in the text

## What I would add next

- A `story.txt` file included in the repo so anyone can run it immediately
- Multiple story files to choose from at the start
- Save the generated story to a new text file automatically
- Detect duplicate placeholders of the same type and only ask once
  — for example if `<noun>` appears 3 times, ask for it once and
  replace all three occurrences with the same word
