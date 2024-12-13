import subprocess
import time

# Function to change the MAC address
def change_mac(interface, mac_address):
    print(f"Changing MAC address of interface {interface} to {mac_address}")
    subprocess.run(["ifconfig", interface, "down"], check=True)
    subprocess.run(["ifconfig", interface, "hw", "ether", mac_address], check=True)
    subprocess.run(["ifconfig", interface, "up"], check=True)

if __name__ == "__main__":
    interface = "eth0"  # Specify your network interface here
    file_name = "listmac"  # File containing list of MAC addresses

    try:
        with open(file_name, "r") as file:
            mac_addresses = [line.strip() for line in file if line.strip()]

        if not mac_addresses:
            print("No MAC addresses found in the file.")
            exit()

        index = 0
        while True:
            new_mac = mac_addresses[index % len(mac_addresses)]
            change_mac(interface, new_mac)
            index += 1
            time.sleep(10)  # Wait for 10 seconds

    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except PermissionError:
        print(f"Permission denied. Please check the permissions for '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
