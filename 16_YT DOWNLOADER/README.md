# Project 16 — YouTube Video Downloader

## What it does

A desktop app that downloads a YouTube video to a folder of your choice.
The user pastes a YouTube URL, a file dialog opens to pick the save
location, and the video downloads in the best available quality.

## What I learned

- How to use `yt_dlp` to download YouTube videos — a configuration
  dictionary (`ydl_opts`) controls the output filename template and
  format quality
- How to use `tkinter.filedialog.askdirectory()` to open a native
  folder selection window instead of asking the user to type a path
- How to use `root.withdraw()` to hide the main tkinter window so
  only the file dialog appears, keeping the program terminal-based
- How to use a `with` statement with `YoutubeDL` so the downloader
  session closes properly after the download finishes
- How to use `%(title)s.%(ext)s` as an output template so the saved
  file is automatically named after the video title with the
  correct file extension

## What was hard

- The tutorial originally used `pytube`, which kept failing —
  YouTube frequently changes its internal API and breaks `pytube`
  until it gets updated, which can take weeks
- Switching to `yt_dlp` instead, which is actively maintained and
  far more reliable for real-world use

## Why I changed the library

The commented-out code at the top is the original `pytube` version
from the tutorial. It did not work reliably, so I rebuilt the same
functionality using `yt_dlp` — a more actively maintained library.
This was my first time deviating from a tutorial to solve a real
problem rather than just following along.

## What I would add next

- Add a progress bar showing download percentage in real time
- Let the user choose video quality instead of always downloading "best"
- Add support for downloading audio only (MP3)
- Validate the URL before attempting to download, with a clear
  error message for invalid links
- Remove the commented-out pytube code before final submission,
  or move it to a separate `archive/` note for reference
