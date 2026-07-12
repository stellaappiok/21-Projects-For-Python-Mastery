# Project 20 — Python Scripting

## What it does

A command-line automation tool that scans a source folder for directories
containing the word "game", copies them to an output folder with cleaned
names, compiles any Go source files it finds inside each folder using the
Go build command, and writes a JSON metadata file summarising all processed
games. Designed to automate a repetitive game build and distribution pipeline.

## What I learned

- How to use `os.scandir()` to efficiently iterate over a directory and
  inspect each item's name and type without loading everything into memory
- How to use `shutil.copytree()` and `shutil.rmtree()` to copy and
  replace entire folder structures in one operation
- How to use `subprocess.run()` with `PIPE` to execute shell commands
  from Python — capturing stdout and stderr and checking return codes
  to determine whether compilation succeeded or failed
- How to use `os.chdir()` with a `try/finally` block to temporarily
  change the working directory for compilation and guarantee the original
  directory is always restored even if an error occurs
- How to write structured JSON metadata using `json.dump()` with
  indentation for human-readable output
- How to use `os.makedirs()` with `exist_ok=True` to safely create
  folders without crashing if they already exist
- How to use `os.path.abspath(__file__)` to build file paths relative
  to the script's own location rather than wherever the terminal happens
  to be running from

## What was hard

- Understanding why `os.chdir()` needed a `try/finally` block — without
  it, a failed compilation would leave the working directory permanently
  changed to the game folder, breaking every subsequent operation
- Getting the subprocess command right — `BUILD_COMMAND + [go_file]`
  combines two lists to form `["go", "build", "filename.go"]` which is
  how subprocess expects multi-argument shell commands

## What I would add next

- Support for multiple languages beyond Go — detect Python, C++, or
  Rust files and compile them with the appropriate command
- A dry run mode that prints what would happen without actually copying
  or compiling anything
- Logging to a file instead of just printing to the terminal
- A config file so source folder, output folder, and search keyword
  can be set without editing the code
