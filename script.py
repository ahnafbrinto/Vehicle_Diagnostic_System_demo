#!/usr/bin/env python3

import subprocess
import re

# Function to get the list of connected devices using arp-scan
def get_connected_devices():
    try:
        # Execute arp-scan command and capture its output
        output = subprocess.check_output(["sudo", "arp-scan", "--localnet"], universal_newlines=True)
        
        # Extract IP addresses and MAC addresses using regular expressions
        devices = re.findall(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F:]+)', output)
        
        return devices
    
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return []

# Function to get the ping round-trip time for a given IP address
def get_ping_time(ip_address):
    try:
        # Execute ping command and capture its output
        output = subprocess.check_output(["ping", "-c", "1", "-W", "1", ip_address], universal_newlines=True)
        
        # Extract round-trip time from the output using regular expressions
        match = re.search(r"time=([\d.]+) ms", output)
        if match:
            # Format the ping time to have three digits before the decimal point
            ping_time = "{:06.2f}".format(float(match.group(1))) + " ms"
            return ping_time
        else:
            return "Down"  # If ping fails or round-trip time is not found
    
    except subprocess.CalledProcessError as e:
        return "Down"  # If ping command fails

# Function to check the status of predefined devices
def check_device_status():
    devices = get_connected_devices()
    # Convert the list of devices into a dictionary for faster lookup
    connected_devices = {ip: mac for ip, mac in devices}
    return connected_devices

if __name__ == "__main__":
    # Check the status of predefined devices
    connected_devices = check_device_status()
    # Predefined list of devices with their IP addresses
    device_status = { 
        "Hood": "192.168.0.9", 
        "Engine": "192.168.0.8", 
        "Front Wheels": "192.168.0.4", 
        "Left Front Door": "192.168.0.5", 
        "Right Front Door": "192.168.0.6", 
        "Left Rear Door": "192.168.0.7", 
        "Right Rear Door": "192.168.0.10", 
        "Trunk Hood": "192.168.0.11", 
        "Rear Wheels": "192.168.0.14", 
        "Back Window": "192.168.0.15", 
        "Cabin": "192.168.0.13", 
        "Center Console": "192.168.0.12",
        "Network Router": "192.168.0.1", # not an iot device 
        "Admin Access IP": "192.168.0.3" # not an iot device
    }
    # Iterate over the predefined device status and print their information
    for device_name, ip_address in device_status.items():
        # Format the IP address to have two digits in each part
        ip_parts = ip_address.split('.')
        formatted_ip = ".".join(part.zfill(2) for part in ip_parts)
        # Check if the device is connected
        if ip_address in connected_devices:
            # Retrieve the MAC address of the connected device
            mac_address = connected_devices[ip_address].upper()  # Convert MAC address to uppercase
            # Get ping time for the device
            ping_time = get_ping_time(ip_address)
            # Print information about the connected device
            print(f" IP: {formatted_ip} - MAC: {mac_address} # Ping: {ping_time} - {device_name}")
        else:
            # Print information about the disconnected device
            print(f" IP: {formatted_ip} - MAC: Under Maintenance # Ping:   FAILED  - {device_name}")
