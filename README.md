# WiFi AutoSwitcher

## Overview
A Python-based utility that automatically switches between saved Wi-Fi networks to maintain the strongest possible connection. The tool monitors signal strengths and switches when a significantly stronger connection is available.

## Features
- **Smart Switching**: Automatically connects to stronger saved Wi-Fi networks.
- **Efficiency Mode**: The scheduled task is optimized to **only run when a network connection is available**, saving battery and resources when offline.
- **Auto-Elevation**: The setup script automatically handles Administrator privileges.
- **Configurable**: Adjustable signal strength threshold (default: 5%).
- **Logging**: Built-in logging to `wifi_switcher.log`.

## File Structure
- `Wifiswitcher.py` - Main Python script with logic.
- `Autoschedule.bat` - **Installer**. Creates a Windows Scheduled Task (runs every 10 mins, persistent).
- `WifiAuto.bat` - Manual runner (console).
- `WifiAutoVB.vbs` - Silent manual runner.

## Prerequisites
- Python 3.9 or higher
- Windows OS
- Saved Wi-Fi profiles (the script only switches to networks you have connected to before).

## Installation & Setup

1. **Install Python**: Ensure Python is installed and added to your System PATH.
2. **Setup the Schedule** (Recommended):
   - Double-click `Autoschedule.bat`.
   - Click "Yes" on the Administrator prompt.
   - The tool is now installed! It will run every 10 minutes in the background, but **only if you are online**.

## Manual Usage
- **Run Once**: Double-click `WifiAuto.bat`.
- **Run Silently**: Double-click `WifiAutoVB.vbs`.

## Configuration
In `Wifiswitcher.py`, you can adjust the sensitivity:
```python
MIN_SIGNAL_STRENGTH_DIFFERENCE_FOR_SWITCHING = 5  # Difference in % required to trigger a switch
```

## Logs & Troubleshooting
The script automatically writes to `wifi_switcher.log` in the same directory. Check this file to see switching history or errors.

**Common Issues:**
- **Access Denied**: The script requires Admin rights to switch networks. The scheduled task handles this automatically with "Highest Privileges".
- **No Switching**: Ensure you have actually connected to the other stronger networks before (they must be "Saved Profiles").

## Limitations
- Windows-only.
- No GUI (runs in background).


## Contributing
Feel free to submit issues and enhancement requests.

## Credits

A huge shoutout to:

- [Reddit Profile - sqrt7744](https://www.reddit.com/user/sqrt7744/) - For igniting the spark of inspiration behind this thrilling project!
  - Original concept from Reddit discussions
  - Source: [Reddit Reply](https://www.reddit.com/r/linux/comments/bbzm9t/automatically_switch_to_the_strongest_wifi_signal/)

Your creativity has fueled our journey! 🚀

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.