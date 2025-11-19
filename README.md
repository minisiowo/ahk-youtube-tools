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

1. **Install required Python libraries:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install AutoHotkey** (if you haven't already)

3. **Run the AutoHotkey script:**
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
  - Copies transcript to clipboard
  - Displays a short success/error message

### Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

## Messages

- **Success**: A notification will appear in the tray
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

## Customization

You can edit the `transcribe.py` file to:
- Change the target folder (currently `~/Desktop/`)
- Change audio/video quality
- Add support for other subtitle languages
- Change output format

## License

This script uses the following libraries:
- yt-dlp - for downloading YouTube videos
- youtube-transcript-api - for fetching subtitles
- pyperclip - for clipboard operations
