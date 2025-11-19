# YouTube Transcript Copier - Prosty narzędzie bez GUI

Szybkie kopiowanie transkrypcji z YouTube jednym skrótem klawiszowym.

## Wymagania

### Python
- Python 3.7 lub nowszy
- pip (menedżer pakietów Python)

### AutoHotkey
- AutoHotkey v2.0 lub nowszy (pobierz z https://www.autohotkey.com/)
- **UWAGA: Wymagana jest wersja 2.0+**

## Instalacja

1. **Zainstaluj wymagane biblioteki Python:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Zainstaluj AutoHotkey** (jeśli jeszcze nie masz)

3. **Uruchom skrypt AutoHotkey:**
   - Kliknij dwukrotnie na `youtube_downloader.ahk`

## Użycie

### Szybka instrukcja
1. Skopiuj URL YouTube do schowka (Ctrl+C)
2. Naciśnij **Win + T**
3. Gotowe! Transkrypcja jest w schowku

### Skrót klawiszowy

- **Win + T** - Pobierz transkrypcję
  - Automatycznie pobiera URL ze schowka
  - Waliduje link YouTube
  - Pobiera transkrypcję (preferuje polski, potem angielski)
  - Kopiuje transkrypcję do schowka
  - Wyświetla krótki komunikat o sukcesie/błędzie

### Obsługiwane formaty URL

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

## Komunikaty

- **Sukces**: Pojawi się powiadomienie w tray'u
- **Błąd**: Pojawi się okienko z opisem problemu

## Pliki w projekcie

- `transcribe.py` - Prosty skrypt Python bez GUI
- `youtube_downloader.ahk` - Skrypt AutoHotkey z jednym skrótem
- `requirements.txt` - Lista wymaganych bibliotek Python
- `README.md` - Ten plik

## Rozwiązywanie problemów

### Błąd: "Brak prawidłowego URL YouTube w schowku"
- Upewnij się, że skopiowałeś link YouTube przed naciśnięciem Win+T

### Błąd: "Python nie jest rozpoznawany"
- Zainstaluj Python lub edytuj `PythonPath` w pliku .ahk

### Błąd przy pobieraniu transkrypcji
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