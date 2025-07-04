# YouTube Downloader - Windows AutoHotkey Version

Ten skrypt pozwala na pobieranie filmów z YouTube, konwertowanie ich na MP3 oraz kopiowanie napisów na Windows przy użyciu AutoHotkey.

## Wymagania

### Python
- Python 3.7 lub nowszy
- pip (menedżer pakietów Python)

### AutoHotkey
- AutoHotkey v2.0 lub nowszy (pobierz z https://www.autohotkey.com/)
- **UWAGA: Wymagana jest wersja 2.0+, nie działa ze starszą wersją v1.1**

### FFmpeg (opcjonalnie)
- FFmpeg jest wymagany do konwersji audio/video
- Pobierz z https://ffmpeg.org/download.html
- Dodaj FFmpeg do PATH

## Instalacja

1. **Zainstaluj wymagane biblioteki Python:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Zainstaluj AutoHotkey** (jeśli jeszcze nie masz)

3. **Uruchom skrypt AutoHotkey:**
   - Kliknij dwukrotnie na `youtube_downloader.ahk`
   - Lub kliknij prawym przyciskiem myszy → "Compile Script" aby utworzyć plik .exe

## Konfiguracja

Jeśli Python nie jest w PATH, edytuj plik `youtube_downloader.ahk` i zmień linię:
```autohotkey
PythonPath := "python"
```
na:
```autohotkey
PythonPath := "C:\Python\python.exe"  ; pełna ścieżka do python.exe
```

## Użycie

### Skróty klawiszowe

- **Win + Y** - Główna funkcja
  - Automatycznie pobiera URL ze schowka jeśli zawiera link YouTube
  - W przeciwnym razie poprosi o podanie URL
  - Wyświetla menu z opcjami: Pobierz film / Pobierz MP3 / Skopiuj napisy

- **Alt + Win + Y** - Uruchom z interfejsem graficznym
  - Otwiera okno dialogowe do wprowadzenia URL i wyboru akcji

- **Ctrl + Win + Y** - Otwórz folder Desktop
  - Szybki dostęp do folderu gdzie zapisywane są pliki

- **Win + F1** - Pokaż pomoc
  - Wyświetla listę dostępnych skrótów

### Sposób działania

1. Skopiuj URL YouTube do schowka
2. Naciśnij **Win + Y**
3. Wybierz akcję z menu:
   - **Pobierz film** - pobiera wideo w formacie MP4
   - **Pobierz MP3** - pobiera tylko audio w formacie MP3
   - **Skopiuj napisy** - kopiuje napisy do schowka

### Obsługiwane formaty URL

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

## Pliki w projekcie

- `transcribe.py` - Główny skrypt Python
- `youtube_downloader.ahk` - Skrypt AutoHotkey
- `requirements.txt` - Lista wymaganych bibliotek Python
- `README.md` - Ten plik z instrukcjami

## Lokalizacja pobieranych plików

Wszystkie pliki są zapisywane na Pulpicie (`~/Desktop/`).

## Rozwiązywanie problemów

### Błąd: "Nie znaleziono pliku skryptu Python"
- Upewnij się, że oba pliki (`transcribe.py` i `youtube_downloader.ahk`) znajdują się w tym samym folderze

### Błąd: "Python nie jest rozpoznawany"
- Zainstaluj Python lub ustaw pełną ścieżkę w `PythonPath`

### Błąd podczas konwersji audio/video
- Zainstaluj FFmpeg i dodaj do PATH

### Błąd: "Błąd przy pobieraniu napisów"
- Nie wszystkie filmy mają dostępne napisy
- Sprawdź czy film ma włączone napisy lub automatyczne napisy

## Customizacja

Możesz edytować plik `transcribe.py` aby:
- Zmienić folder docelowy (aktualnie `~/Desktop/`)
- Zmienić jakość audio/video
- Dodać obsługę innych języków napisów
- Zmienić format wyjściowy

## Licencja

Ten skrypt używa następujących bibliotek:
- yt-dlp - do pobierania filmów z YouTube
- youtube-transcript-api - do pobierania napisów
- pyperclip - do operacji na schowku