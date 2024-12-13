import re

# List of MAC addresses
mac_addresses = [
    "53:1d:3e:19:56:0d", "11:8d:0a:6d:39:87", "invalid:mac:addr",
    # Add all other MAC addresses here...
    "a3:6a:f7:eb:0a:ce"
]

# Regex pattern for valid MAC address
mac_pattern = re.compile(r'^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$')

# Filter valid MAC addresses
valid_macs = [mac for mac in mac_addresses if mac_pattern.match(mac)]

# Count valid MAC addresses
valid_count = len(valid_macs)

# Output results
print(f"Valid MAC addresses: {valid_count}")
print("Filtered valid MAC addresses:")
print(valid_macs)
