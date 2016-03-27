i = 5
Do Until i=10
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "end.bat" & Chr(34), 0
Set WshShell = Nothing
WScript.Sleep 10000 
Loop