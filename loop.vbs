i=5
Do Until i=10
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "go.bat" & Chr(34), 0
Set WshShell = Nothing
WScript.Sleep 20000 
Loop