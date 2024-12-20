@echo off
REM Define variables
set scriptPath=C:\Users\USER\AppData\Local\Programs\Python\Python39\python.exe
set pythonScript=C:\Users\USER\Desktop\Wifiswitcher.py
set taskName=WifiAutoSwitcher
set taskDescription=Automatically switches Wi-Fi networks

REM Delete the task if it already exists
schtasks /delete /tn "%taskName%" /f

REM Create the scheduled task to run the Python script
schtasks /create /tn "%taskName%" /tr "\"%scriptPath%\" \"%pythonScript%\"" /sc minute /mo 10 /f /rl highest /v1

REM Optional: Display confirmation message
echo Task '%taskName%' created successfully to run every 15 minutes.


:: Wait for 5 seconds
timeout /t 5 /nobreak

:: Exit after 5 seconds
exit

