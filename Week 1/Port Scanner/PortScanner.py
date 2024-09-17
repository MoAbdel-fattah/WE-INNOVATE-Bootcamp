import socket
import time

def scan_ports(target, port_start, port_end):
    start_time = time.time()

    for port in range(port_start, port_end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is open on {target}")

    end_time = time.time()
    print(f"Scan completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    try:
        target = input("Please enter the target IP address: ")
        port_start = int(input("Please enter the starting port number: "))
        port_end = int(input("Please enter the ending port number: "))

        if port_start < 1 or port_start > 65535 or port_end < 1 or port_end > 65535:
            raise ValueError("Invalid port numbers")

        print(f"Scanning ports {port_start} to {port_end} on {target}")
        scan_ports(target, port_start, port_end)

    except ValueError as e:
        print(f"Error: {e}")
    except socket.error as e:
        print(f"Error: {e}")