; YouTube Transcript Copier AutoHotkey v2 Script
; Skrót klawiszowy: Win + Y

#Requires AutoHotkey v2.0
#SingleInstance Force
SendMode("Input")
SetWorkingDir(A_ScriptDir)

; Ustawienia
PythonPath := A_ScriptDir . "\.venv\Scripts\pythonw.exe"
ScriptPath := A_ScriptDir . "\transcribe.py"
TimeoutMs := 30000

; Główny skrót klawiszowy - Win + Y
#y::
{
    ; Natychmiastowa informacja, że skrót zadziałał
    ToolTip("Downloading transcript...")

    ; Uruchom skrypt Python
    try {
        output := ""
        errorOutput := ""
        shell := ComObject("WScript.Shell")
        
        ; Poprawne cytowanie ścieżek ze spacjami
        command := '"' . PythonPath . '" "' . ScriptPath . '"'
        exec := shell.Exec(command)
        
        ; Czekaj na zakończenie, ale nie dłużej niż TimeoutMs
        startTime := A_TickCount
        while (exec.Status = 0) {
            if (A_TickCount - startTime > TimeoutMs) {
                exec.Terminate()
                ToolTip()
                MsgBox("Timed out after " . (TimeoutMs // 1000) . " s. Check your internet connection.", "Error", "16")
                return
            }
            Sleep(100)
        }

        ; Zbierz output
        output := exec.StdOut.ReadAll()
        errorOutput := exec.StdErr.ReadAll()
        
        ToolTip()

        ; Wyświetl komunikat w zależności od wyniku
        if (InStr(output, "SUCCESS")) {
            ; ToolTip jest zawsze widoczny, nawet gdy powiadomienia Windows są wyciszone
            ToolTip("Transcript copied to clipboard")
            SetTimer(() => ToolTip(), -3000)
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
        ToolTip()
        MsgBox("Error running script: " . err.message, "Error", "16")
    }
}
