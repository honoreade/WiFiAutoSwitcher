@echo off

REM Define variables using current directory
set scriptPath=python
set pythonScript=%~dp0Wifiswitcher.py
set taskName=WifiAutoSwitcher

REM Delete existing task if present
schtasks /delete /tn "%taskName%" /f

REM Create the scheduled task to run the Python script
schtasks /create /tn "%taskName%" /tr "\"%scriptPath%\" \"%pythonScript%\"" /sc minute /mo 10 /f /rl highest /v1

REM Optional: Display confirmation message
echo Task '%taskName%' created successfully to run every 10 minutes.

REM Wait for 5 seconds
timeout /t 5 /nobreak

REM Exit after 5 seconds
exit
