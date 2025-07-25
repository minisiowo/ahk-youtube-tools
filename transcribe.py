#!/usr/bin/env python3

# YouTube Transcript Copier - Windows version with AutoHotkey support
# Supports transcript copying only

import sys
import os
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import pyperclip
import tkinter as tk
from tkinter import messagebox, simpledialog


def get_video_id(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]
    elif parsed_url.hostname in ["youtu.be"]:
        return parsed_url.path[1:]
    return None


def copy_transcript(video_id):
    """Kopiuje napisy z YouTube"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=["pl", "en"]
        )
        text = " ".join(item["text"].replace("\n", "") for item in transcript)
        pyperclip.copy(text)
        show_message("Sukces", "Napisy skopiowane do schowka!")
    except Exception as e:
        show_message("Błąd", f"Błąd przy pobieraniu napisów: {str(e)}")


def show_message(title, message):
    """Wyświetla komunikat w GUI"""
    root = tk.Tk()
    root.withdraw()  # Ukryj główne okno
    messagebox.showinfo(title, message)
    root.destroy()


def get_user_input():
    """Pobiera URL od użytkownika przez GUI"""
    root = tk.Tk()
    root.withdraw()  # Ukryj główne okno
    
    # Pobierz URL
    url = simpledialog.askstring("YouTube Transcript Copier", "Podaj URL YouTube:")
    if not url:
        return None
    
    return url


def main():
    # Sprawdź czy URL został przekazany z linii poleceń
    if len(sys.argv) >= 2:
        url = sys.argv[1]
        # Dla kompatybilności z AutoHotkey, jeśli podano drugi argument, ignoruj go
        # (wcześniej był to numer akcji, teraz zawsze kopiujemy transkrypcję)
    else:
        # Użyj GUI do pobrania URL
        url = get_user_input()
    
    if not url:
        show_message("Błąd", "Anulowano operację.")
        return

    video_id = get_video_id(url)
    if not video_id:
        show_message("Błąd", "Podany URL jest niepoprawny. Spróbuj ponownie.")
        return

    # Zawsze kopiuj transkrypcję
    copy_transcript(video_id)


if __name__ == "__main__":
    main()