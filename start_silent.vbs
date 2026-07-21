Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c cd /d ""C:\My Projects\Vlora"" && python launcher.py", 0, False