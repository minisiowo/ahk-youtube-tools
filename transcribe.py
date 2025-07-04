#!/usr/bin/env python3

# YouTube Downloader - Windows version with AutoHotkey support
# Supports video download, audio download, and transcript copying

import sys
import os
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import pyperclip
import tkinter as tk
from tkinter import messagebox, simpledialog

# Konfiguracja opcji pobierania wideo
yt_dlp_opts_video = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "outtmpl": os.path.expanduser("~/Desktop/%(title)s.%(ext)s"),
    "postprocessors": [
        {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",  # Wymuszenie na mp4, jeśli konwersja jest konieczna
        }
    ],
}

# Konfiguracja opcji pobierania audio
yt_dlp_opts_audio = {
    "format": "bestaudio/best",
    "outtmpl": os.path.expanduser("~/Desktop/%(title)s.%(ext)s"),
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


def get_video_id(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]
    elif parsed_url.hostname in ["youtu.be"]:
        return parsed_url.path[1:]
    return None


def download_video(url):
    """Pobiera wideo z YouTube"""
    try:
        with yt_dlp.YoutubeDL(yt_dlp_opts_video) as ydl:
            ydl.download([url])
        show_message("Sukces", "Wideo pobrane pomyślnie!")
    except Exception as e:
        show_message("Błąd", f"Błąd przy pobieraniu wideo: {str(e)}")


def download_audio(url):
    """Pobiera audio z YouTube"""
    try:
        with yt_dlp.YoutubeDL(yt_dlp_opts_audio) as ydl:
            ydl.download([url])
        show_message("Sukces", "Audio pobrane pomyślnie!")
    except Exception as e:
        show_message("Błąd", f"Błąd przy pobieraniu audio: {str(e)}")


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
    """Pobiera dane od użytkownika przez GUI"""
    root = tk.Tk()
    root.withdraw()  # Ukryj główne okno
    
    # Pobierz URL
    url = simpledialog.askstring("YouTube Downloader", "Podaj URL YouTube:")
    if not url:
        return None, None
    
    # Pobierz akcję
    action_root = tk.Tk()
    action_root.title("Wybierz akcję")
    action_root.geometry("300x150")
    action_root.resizable(False, False)
    
    # Wycentruj okno
    action_root.eval('tk::PlaceWindow . center')
    
    selected_action = tk.StringVar(value="")
    
    def select_action(action):
        selected_action.set(action)
        action_root.destroy()
    
    tk.Label(action_root, text="Wybierz akcję:", font=("Arial", 12)).pack(pady=10)
    
    tk.Button(action_root, text="Pobierz film", command=lambda: select_action("1"), width=20).pack(pady=5)
    tk.Button(action_root, text="Pobierz MP3", command=lambda: select_action("2"), width=20).pack(pady=5)
    tk.Button(action_root, text="Skopiuj napisy", command=lambda: select_action("3"), width=20).pack(pady=5)
    
    action_root.mainloop()
    
    return url, selected_action.get()


def main():
    # Sprawdź czy argumenty zostały przekazane z linii poleceń
    if len(sys.argv) >= 3:
        url = sys.argv[1]
        user_input = sys.argv[2]
    else:
        # Użyj GUI do pobrania danych
        url, user_input = get_user_input()
    
    if not url or not user_input:
        show_message("Błąd", "Anulowano operację.")
        return

    video_id = get_video_id(url)
    if not video_id:
        show_message("Błąd", "Podany URL jest niepoprawny. Spróbuj ponownie.")
        return

    if user_input == "1":
        download_video(url)
    elif user_input == "2":
        download_audio(url)
    elif user_input == "3":
        copy_transcript(video_id)
    else:
        show_message("Błąd", "Nieznana opcja, spróbuj ponownie...")


if __name__ == "__main__":
    main()