import subprocess

MIN_SIGNAL_STRENGTH_DIFFERENCE_FOR_SWITCHING = 5  # Minimum signal strength difference to trigger a switch

def run_subprocess(command):
    """Run a subprocess command and return the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command {command}: {e}")
        return ""

def get_saved_profiles():
    """Get a list of saved Wi-Fi profiles."""
    output = run_subprocess(['netsh', 'wlan', 'show', 'profiles'])
    profiles = [line.split(":")[1].strip() for line in output.splitlines() if "All User Profile" in line]
    return profiles

def get_wifi_networks():
    """Get a list of available Wi-Fi networks and their signal strengths."""
    return run_subprocess(['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'])

def parse_networks(networks_info):
    """Parse available networks and their signal strengths."""
    networks = []
    lines = networks_info.splitlines()
    ssid, signal_strength = None, None
    for line in lines:
        line = line.strip()
        if "SSID" in line and "BSSID" not in line:  # Avoid BSSID lines
            ssid = line.split(":")[1].strip()
        if "Signal" in line:
            signal_strength = int(line.split(":")[1].strip().replace("%", ""))
            if ssid is not None:  # Only add if SSID exists
                networks.append((ssid, signal_strength))
                ssid, signal_strength = None, None  # Reset for next network
    return networks

def get_current_connection():
    """Get the current Wi-Fi connection and signal strength."""
    output = run_subprocess(['netsh', 'wlan', 'show', 'interfaces'])
    ssid, signal_strength = "", 0
    for line in output.splitlines():
        line = line.strip()
        if "SSID" in line and "BSSID" not in line:  # Ensure it’s the full SSID, not the BSSID (MAC address)
            ssid = line.split(":")[1].strip()
        if "Signal" in line:
            signal_strength = int(line.split(":")[1].strip().replace("%", ""))
    return ssid, signal_strength

def find_saved_available_networks_with_strength():
    """Find currently available Wi-Fi networks that are also saved and include signal strength."""
    available_networks_info = get_wifi_networks()
    available_networks = parse_networks(available_networks_info)
    saved_profiles = get_saved_profiles()
    return [(ssid, signal) for ssid, signal in available_networks if ssid in saved_profiles]

def switch_to_strongest_network(networks, saved_profiles, current_signal_strength):
    """Switch to the strongest saved network."""
    networks.sort(key=lambda x: x[1], reverse=True)  # Sort by signal strength, highest first
    for ssid, signal in networks:
        if ssid in saved_profiles and signal > current_signal_strength + MIN_SIGNAL_STRENGTH_DIFFERENCE_FOR_SWITCHING:
            print(f"Switching to {ssid} with signal {signal}%")
            result = subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Successfully switched to {ssid}")
                return ssid
            else:
                print(f"Failed to switch to {ssid}: {result.stderr}")
    print("No stronger network found.")
    return None

def main():
    """Main function to manage Wi-Fi connections."""
    current_ssid, current_signal_strength = get_current_connection()
    if not current_ssid:
        print("No active Wi-Fi connection. Exiting...")
        return

    saved_available_networks = find_saved_available_networks_with_strength()
    print("-------------------Wi-Fi Auto Switcher------------------")
    print(f"\nCurrently Available Saved Networks: {len(saved_available_networks)}")
    for ssid, signal in saved_available_networks:
        print(f"{ssid}: {signal}%")

    print(f"Current network before switch: {current_ssid}, Signal strength: {current_signal_strength}%")
    if saved_available_networks:
        switch_to_strongest_network(saved_available_networks, get_saved_profiles(), current_signal_strength)

    updated_ssid, updated_signal_strength = get_current_connection()
    print(f"Current network after switch: {updated_ssid}, Signal strength: {updated_signal_strength}%")

if __name__ == "__main__":
    main()
