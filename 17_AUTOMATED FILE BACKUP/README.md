# Project 17 — Automated File Backup

## What it does

A background script that automatically backs up an entire folder to a
destination directory once every day at a scheduled time. Each backup is
saved in its own dated folder, so you build a daily history of snapshots
rather than overwriting the previous backup.

## What I learned

- How to use `shutil.copytree()` to recursively copy an entire folder
  and all of its contents to a new location in one line
- How to use `datetime.date.today()` to generate a folder name based
  on the current date, creating automatic version history
- How to use `os.path.join()` to build file paths correctly across
  different operating systems instead of manually concatenating strings
- How to use the `schedule` library to run a function automatically
  at a specific time every day — `schedule.every().day.at("12:00")`
- How to use a `while True` loop combined with `schedule.run_pending()`
  to keep a script alive and checking for scheduled tasks continuously
- How to use `time.sleep()` inside the loop so the program checks the
  schedule periodically instead of running constantly at full speed
- How to catch a `FileExistsError` so the script does not crash if a
  backup for that date already exists

## What was hard

- Understanding that `schedule.run_pending()` does nothing by itself —
  it only checks if a scheduled job is due, so it needs to sit inside
  a loop that runs continuously for the schedule to ever trigger
- Realising the script must keep running in the background at all
  times for the schedule to work — closing the terminal stops everything

## What I would add next

- Set `source_dir` and `destination_dir` using environment variables
  or a config file instead of hardcoding empty strings that must be
  filled in manually
- Add logging to a file so backup history can be reviewed later
  without watching the terminal
- Delete backups older than a set number of days to avoid filling
  up the destination drive over time
- Add email or desktop notification when a backup succeeds or fails
- Allow scheduling multiple times per day or different days of the week
