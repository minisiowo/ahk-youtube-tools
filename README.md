# YouTube Transcript Copier

Quickly copy YouTube transcripts with a single keyboard shortcut.

## Requirements

### Python
- Python 3.7 or newer
- pip (Python package manager)

### AutoHotkey
- AutoHotkey v2.0 or newer (download from https://www.autohotkey.com/)
- **NOTE: Version 2.0+ is required**

## Installation

1. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

2. **Install required Python libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install AutoHotkey** (if you haven't already)

4. **Run the AutoHotkey script:**
   - Double-click on `youtube_downloader.ahk`

## Usage

### Quick Start
1. Copy a YouTube URL to the clipboard (Ctrl+C)
2. Press **Win + Y**
3. Done! The transcript is in your clipboard

### Keyboard Shortcut

- **Win + Y** - Download transcript
  - Automatically retrieves URL from clipboard
  - Validates YouTube link
  - Fetches transcript (prefers Polish, then English)
  - If that fails, retries with yt-dlp as a fallback
  - Copies transcript to clipboard
  - Displays a short success/error message

### Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID` (also `m.youtube.com` and `music.youtube.com`)
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`
- `https://www.youtube.com/live/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

## Messages

- **In progress**: A "Downloading transcript..." tooltip appears next to the cursor
- **Success**: A tooltip and a tray notification confirm the transcript was copied
- **Error**: A popup window with the problem description will appear

## Project Files

- `transcribe.py` - Simple Python script without GUI
- `youtube_downloader.ahk` - AutoHotkey script with a single shortcut
- `requirements.txt` - List of required Python libraries
- `README.md` - This file

## Troubleshooting

### Error: "No valid YouTube URL in clipboard"
- Make sure you copied a YouTube link before pressing Win+Y

### Error: "Python is not recognized"
- Install Python or edit `PythonPath` in the .ahk file

### Error fetching transcript
- Not all videos have subtitles available
- Check if the video has subtitles or auto-generated captions enabled

### Error: "YouTube is temporarily blocking requests from your IP"
- YouTube rate-limits unofficial subtitle requests; the block usually lifts after a few hours
- Try again later or from another network (e.g. a phone hotspot); disable your VPN if you use one
- If the message says the yt-dlp fallback was blocked too, see [Using cookies](#using-cookies)

### Error: "Timed out"
- The download is stopped after 30 seconds (`TimeoutMs` in the .ahk file)
- Check your internet connection

## Using cookies

When YouTube asks yt-dlp to "confirm you're not a bot", the fallback can use cookies from your browser:

1. Export your YouTube cookies in Netscape format (e.g. with a "cookies.txt" browser extension) while signed in to YouTube
2. Save the file as `cookies.txt` next to `transcribe.py`

`cookies.txt` is in `.gitignore`. Never commit or share it, because it gives access to your Google account.

## Customization

- Edit `LANGUAGES` in `transcribe.py` to change the preferred subtitle languages
- Edit `TimeoutMs` in `youtube_downloader.ahk` to change the download timeout
- Edit the `#y::` line in `youtube_downloader.ahk` to change the keyboard shortcut

## License

This script uses the following libraries:
- youtube-transcript-api - for fetching subtitles
- yt-dlp - fallback for fetching subtitles
- pyperclip - for clipboard operations
