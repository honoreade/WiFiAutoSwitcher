@echo off

REM Check for Administrator privileges
fltmc >nul 2>&1 || (
    echo Requesting Administrator privileges...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit /b
)

REM Define variables using current directory
set scriptPath=python
set pythonScript=%~dp0Wifiswitcher.py
set taskName=WifiAutoSwitcher

REM Delete existing task if present (suppress errors if it doesn't exist)
schtasks /delete /tn "%taskName%" /f >nul 2>&1

REM Create the scheduled task to run the Python script
schtasks /create /tn "%taskName%" /tr "\"%scriptPath%\" \"%pythonScript%\"" /sc minute /mo 10 /f /rl highest
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to create scheduled task.
    pause
    exit /b
)

REM Update task settings to run only when network is available (Computationally efficient)
powershell -Command "Set-ScheduledTask -TaskName '%taskName%' -Settings (New-ScheduledTaskSettingsSet -RunOnlyIfNetworkAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable)"

REM Optional: Display confirmation message
echo Task '%taskName%' created successfully to run every 10 minutes.

REM Wait for 5 seconds
timeout /t 5 /nobreak

REM Exit after 5 seconds
exit
