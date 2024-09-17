# Port Scanner
## Purpose
- This Python script is designed to scan a specified range of ports on a given target IP address. It uses the socket module to create TCP sockets and attempt connections to each port. If a connection is successful, the script prints a message indicating that the port is open.

## Usage
1. Clone or download the repository.
2. Install dependencies: Ensure you have Python installed. You might also need to install additional libraries if they're not already included.
3. Run the script: Execute the Python script using your preferred method.
4. Enter target information: When prompted, provide the target IP address and the desired port range.

## Example
```python
python port_scanner.py
Please enter the target IP address: 192.168.1.100
Please enter the starting port number: 1
Please enter the ending port number: 1000
Scanning ports 1 to 1000 on 192.168.1.100
Port 22 is open on 192.168.1.100
Port 80 is open on 192.168.1.100
Port 443 is open on 192.168.1.100
Scan completed in 1.23 seconds
```
## Features
- Port scanning: Scans a specified range of ports on a target IP address.
- Error handling: Handles potential errors like invalid IP addresses or port numbers.
- Timeout: Sets a timeout to prevent indefinite blocking.
Performance: Measures and displays the scan completion time.
Customization
- Port range: Modify the port_start and port_end variables to scan different ranges.
- Timeout: Adjust the timeout value in the s.settimeout(1) line.
- Output: Customize the output format or add additional information.
## Notes
- This script is a basic implementation and might not be suitable for large-scale or intensive scanning.
- For more advanced scanning or security purposes, consider using specialized tools or libraries.
- Be mindful of network policies and ethical considerations when scanning ports on remote systems.