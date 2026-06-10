# Project 05 — Password Manager

## What it does

A terminal-based password manager that securely stores and retrieves
account credentials. Passwords are encrypted before being saved to a
file and decrypted only when viewed. The user can add new passwords
or view existing ones in a continuous session until they quit.

## What I learned

- How to use the `cryptography` library and `Fernet` symmetric encryption
  to encrypt and decrypt sensitive data
- How to load an encryption key from a file and use it consistently
  across sessions so stored passwords can always be decrypted
- How to read and write to files using `open()` in both read and append mode
- How to use a `while True` loop to keep a program running until the
  user explicitly quits
- How to split stored data using a delimiter (`|`) to separate fields
- How to handle errors gracefully using `try/except` so one corrupted
  entry does not crash the entire program

## What was hard

- Understanding how Fernet encryption works — the key must be the same
  key used to encrypt, otherwise decryption fails completely
- Handling the encoding correctly — Fernet works with bytes, not strings,
  so `.encode()` and `.decode()` had to be used carefully in the right places
- Making the view function robust enough to skip malformed lines without
  crashing

## What I would add next

- A `generate_key()` function that creates and saves a new key if one
  does not already exist, so the setup is fully self-contained
- A `delete` option to remove a saved entry by account name
- A search function to find a specific account without viewing all entries
- Master password protection so the manager itself requires authentication
  before anyone can use it
