; YouTube Transcript Copier AutoHotkey v2 Script
; Skrót klawiszowy: Win + T

#Requires AutoHotkey v2.0
#SingleInstance Force
SendMode("Input")
SetWorkingDir(A_ScriptDir)

; Ustawienia
PythonPath := A_ScriptDir . "\.venv\Scripts\pythonw.exe"
ScriptPath := A_ScriptDir . "\transcribe.py"

; Główny skrót klawiszowy - Win + Y
#y::
{
    ; Uruchom skrypt Python
    try {
        output := ""
        errorOutput := ""
        shell := ComObject("WScript.Shell")
        
        ; Poprawne cytowanie ścieżek ze spacjami
        command := '"' . PythonPath . '" "' . ScriptPath . '"'
        exec := shell.Exec(command)
        
        ; Czekaj na zakończenie i zbierz output
        output := exec.StdOut.ReadAll()
        errorOutput := exec.StdErr.ReadAll()
        
        ; Wyświetl komunikat w zależności od wyniku
        if (InStr(output, "SUCCESS")) {
            TrayTip("Transcript downloaded", "Transcript has been copied to clipboard", 1)
        } else if (InStr(output, "ERROR") || errorOutput != "") {
            ; Wyciągnij treść błędu
            errorMsg := (errorOutput != "") ? errorOutput : RegExReplace(output, "ERROR:\s*", "")
            MsgBox(errorMsg, "Error", "16")
        } else if (output != "") {
            ; Pokaż cały output jeśli nie ma standardowego komunikatu
            MsgBox(output, "Result", "64")
        }
    } catch Error as err {
        MsgBox("Error running script: " . err.message, "Error", "16")
    }
}
