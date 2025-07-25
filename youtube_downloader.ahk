; YouTube Transcript Copier AutoHotkey v2 Script
; Skrót klawiszowy: Win + Y

#Requires AutoHotkey v2.0
#SingleInstance Force
SendMode("Input")
SetWorkingDir(A_ScriptDir)

; Ustawienia
PythonPath := "python"
ScriptPath := A_ScriptDir . "\transcribe.py"

; Globalna zmienna dla URL
CurrentURL := ""

; Główny skrót klawiszowy - Win + Y
#y::
{
    ; Debugowanie - pokaż komunikat że hotkey działa
    ; MsgBox("Hotkey Win+Y aktywowany", "Debug", "64 T1")
    
    ; Pobierz URL ze schowka
    ClipboardURL := A_Clipboard
    
    ; Sprawdź czy schowek zawiera URL YouTube
    if (InStr(ClipboardURL, "youtube.com") || InStr(ClipboardURL, "youtu.be")) {
        ShowActionMenu(ClipboardURL)
    } else {
        try {
            UserURL := InputBox("Podaj URL YouTube:", "YouTube Transcript Copier", "w400 h130")
            if (UserURL.Result != "Cancel" && UserURL.Value != "") {
                ShowActionMenu(UserURL.Value)
            }
        } catch Error as err {
            MsgBox("Błąd podczas pobierania URL: " . err.message, "Błąd", "16")
        }
    }
}

; Funkcja do wyświetlania menu akcji
ShowActionMenu(URL)
{
    global CurrentURL
    CurrentURL := URL
    
    ; Usuń poprzednie menu jeśli istnieje
    try {
        ActionMenu := Menu()
    } catch {
        ; Ignoruj błędy jeśli menu nie istnieje
    }
    
    ActionMenu := Menu()
    ActionMenu.Add("Skopiuj napisy", (*) => RunPythonScript(URL, "3"))
    ActionMenu.Add()
    ActionMenu.Add("Anuluj", (*) => "")
    
    ActionMenu.Show()
}

; Funkcja do uruchamiania skryptu Python
RunPythonScript(URL, Action)
{
    ; Sprawdź czy plik Python istnieje
    if (!FileExist(ScriptPath)) {
        MsgBox("Nie znaleziono pliku skryptu Python:`n" . ScriptPath, "Błąd", "16")
        return
    }
    
    ; Pokaż komunikat o rozpoczęciu procesu
    ActionText := ""
    switch Action {
        case "3": ActionText := "Kopiowanie napisów..."
    }
    
    ; Utwórz komendę
    Command := PythonPath . ' "' . ScriptPath . '" "' . URL . '" ' . Action
    
    ; Uruchom skrypt w tle
    try {
        RunWait(Command, , "Hide")
    } catch Error as err {
        MsgBox("Błąd podczas uruchamiania skryptu:`n" . err.message, "Błąd", "16")
    }
}

; Alt + Win + Y - szybkie uruchomienie z GUI
!#y::
{
    RunWait(PythonPath . ' "' . ScriptPath . '"', , "Hide")
}

; Ctrl + Win + Y - otwórz folder Desktop
^#y::
{
    Run('explorer.exe "' . A_Desktop . '"')
}

; Win + F1 - Pokaż help
#F1::
{
    HelpText := "YouTube Transcript Copier - Skróty klawiszowe:`n`n"
    HelpText .= "Win + Y          - Skopiuj napisy`n"
    HelpText .= "Alt + Win + Y    - Uruchom z GUI`n"
    HelpText .= "Ctrl + Win + Y   - Otwórz folder Desktop`n"
    HelpText .= "Win + F1         - Pokaż tę pomoc`n`n"
    HelpText .= "Obsługiwane formaty URL:`n"
    HelpText .= "- https://www.youtube.com/watch?v=...`n"
    HelpText .= "- https://youtu.be/...`n`n"
    HelpText .= "Napisy są kopiowane do schowka."
    
    MsgBox(HelpText, "YouTube Transcript Copier - Pomoc", "64")
}

; Ctrl + Alt + H - Info o skrypcie
^!h::
{
    InfoText := "YouTube Transcript Copier AutoHotkey Script`n`n"
    InfoText .= "Funkcje:`n"
    InfoText .= "- Kopiowanie napisów z YouTube do schowka`n`n"
    InfoText .= "Skróty:`n"
    InfoText .= "Win + Y - Uruchom główną funkcję`n"
    InfoText .= "Alt + Win + Y - Uruchom GUI`n"
    InfoText .= "Ctrl + Win + Y - Otwórz folder Desktop`n"
    InfoText .= "Win + F1 - Pomoc`n`n"
    InfoText .= "Ścieżka Python: " . PythonPath . "`n"
    InfoText .= "Ścieżka skryptu: " . ScriptPath
    
    MsgBox(InfoText, "YouTube Transcript Copier Info", "64")
}
