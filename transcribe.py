#!/usr/bin/env python3

# YouTube Transcript Copier - prosty skrypt bez GUI
# Pobiera link ze schowka i kopiuje transkrypcję

import re
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import pyperclip


def get_video_id(url):
    """Wyciąga ID video z URL YouTube"""
    parsed_url = urlparse(url)
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]
    elif parsed_url.hostname in ["youtu.be"]:
        return parsed_url.path[1:]
    return None


def main():
    # Pobierz URL ze schowka
    url = pyperclip.paste().strip()
    
    # Walidacja URL
    if not url or not ("youtube.com" in url or "youtu.be" in url):
        print("BŁĄD: Brak prawidłowego URL YouTube w schowku")
        return
    
    # Wyciągnij ID video
    video_id = get_video_id(url)
    if not video_id:
        print("BŁĄD: Nieprawidłowy URL YouTube")
        return
    
    # Pobierz transkrypcję
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id, languages=["pl", "en"])
        text = re.sub(r'\s+', ' ', " ".join([snippet.text for snippet in fetched_transcript.snippets]))
        
        # Skopiuj do schowka
        pyperclip.copy(text)
        print("SUKCES: Transkrypcja skopiowana do schowka")
    except Exception as e:
        print(f"BŁĄD: {str(e)}")


if __name__ == "__main__":
    main()