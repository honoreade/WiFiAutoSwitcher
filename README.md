# WiFi AutoSwitcher

## Overview
A Python-based utility that automatically switches between saved Wi-Fi networks to maintain the strongest possible connection. The tool monitors signal strengths and switches when a significantly stronger connection is available.

## Features
- Automatic switching to stronger Wi-Fi networks
- Minimum signal strength difference threshold (default: 5%)
- Support for all saved Wi-Fi profiles
- Silent running mode via VBScript
- Automated scheduling via Windows Task Scheduler

## File Structure
- `Wifiswitcher.py` - Main Python script
- `WifiAuto.bat` - Batch wrapper with timeout
- `WifiAutoVB.vbs` - Silent execution script
- `Autoschedule.bat` - Task scheduler configuration

## Prerequisites
- Python 3.9 or higher
- Windows OS with `netsh` command support
- Administrative privileges

## Installation

1. Create a new folder for the project:
```bash
mkdir WiFiAutoSwitcher
cd WiFiAutoSwitcher
```

2. Copy all files into this folder:
- Wifiswitcher.py
- WifiAuto.bat
- WifiAutoVB.vbs
- Autoschedule.bat

3. Make sure Python is installed and in your system PATH
   - Download from python.org if needed
   - During installation, check "Add Python to PATH"

4. Test the installation:
```bash
python Wifiswitcher.py
```

## Important Path Setup
1. Ensure Python is added to System PATH during installation
2. All scripts must be in the same folder
3. Run scripts from within their folder

## Usage

### Simple Method
1. Double-click `WifiAuto.bat` to run with console
2. Double-click `WifiAutoVB.vbs` to run silently

### Automatic Schedule
1. Right-click `Autoschedule.bat`
2. Select "Run as administrator"
3. Task will run every 10 minutes

## Configuration
In `Wifiswitcher.py`, adjust the minimum signal strength difference required for switching:
```python
MIN_SIGNAL_STRENGTH_DIFFERENCE_FOR_SWITCHING = 5  # Change as needed
```

## Sample Output
```
-------------------Wi-Fi Auto Switcher------------------

Currently Available Saved Networks: 2
HomeNetwork: 85%
OfficeWiFi: 70%

Current network before switch: HomeNetwork, Signal strength: 85%
No stronger network found.
Current network after switch: HomeNetwork, Signal strength: 85%
```

## Troubleshooting

### Common Issues
1. **Permission Denied**
   - Run scripts as Administrator
   - Ensure Python has network access permissions

2. **Path Errors**
   - Verify Python path in all script files
   - Check script locations match paths in batch files

3. **Task Scheduler Issues**
   - Confirm task is running with highest privileges
   - Verify user account has appropriate permissions

### Logging
Enable basic logging by redirecting output:
```bat
python Wifiswitcher.py > wifi_log.txt 2>&1
```

## Security Notes
- Scripts require administrator privileges for network operations
- All networks must be pre-saved in Windows
- No password handling or storage implemented

## Limitations
- Windows-only support
- Requires saved network profiles
- No GUI interface
- Minimal error handling

## Contributing
Feel free to submit issues and enhancement requests.