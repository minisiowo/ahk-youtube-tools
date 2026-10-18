#!/usr/bin/env python3

# YouTube Transcript Copier - prosty skrypt bez GUI
# Pobiera link ze schowka i kopiuje transkrypcję

import re
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import pyperclip


YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com"}
VIDEO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")


def get_video_id(url):
    """Wyciąga ID video z URL YouTube"""
    if "://" not in url:
        url = "https://" + url
    parsed_url = urlparse(url)
    hostname = (parsed_url.hostname or "").lower()
    path_parts = [part for part in parsed_url.path.split("/") if part]

    video_id = None
    if hostname in YOUTUBE_HOSTS:
        if parsed_url.path == "/watch":
            video_id = parse_qs(parsed_url.query).get("v", [None])[0]
        elif len(path_parts) >= 2 and path_parts[0] in ("shorts", "live", "embed", "v"):
            video_id = path_parts[1]
    elif hostname == "youtu.be" and path_parts:
        video_id = path_parts[0]

    if video_id and VIDEO_ID_PATTERN.match(video_id):
        return video_id
    return None


def main():
    # Pobierz URL ze schowka
    url = pyperclip.paste().strip()

    # Walidacja URL
    if not url or not ("youtube.com" in url or "youtu.be" in url):
        print("ERROR: No valid YouTube URL in clipboard")
        return

    # Wyciągnij ID video
    video_id = get_video_id(url)
    if not video_id:
        print("ERROR: Invalid YouTube URL")
        return

    # Pobierz transkrypcję
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id, languages=["pl", "en"])
        text = re.sub(r'\s+', ' ', " ".join([snippet.text for snippet in fetched_transcript.snippets]))

        # Skopiuj do schowka
        pyperclip.copy(text)
        print("SUCCESS: Transcript copied to clipboard")
    except Exception as e:
        print(f"ERROR: {str(e)}")


if __name__ == "__main__":
    # Znaki spoza strony kodowej konsoli zamieniamy na "?" zamiast przerywać skrypt wyjątkiem
    for stream in (sys.stdout, sys.stderr):
        if stream is not None:
            stream.reconfigure(errors="replace")
    main()
