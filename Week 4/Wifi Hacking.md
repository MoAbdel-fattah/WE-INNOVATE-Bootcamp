## **Understanding WiFi Network Terms**

**WPA:** Wi-Fi Protected Access is a Wi-Fi protocol that has better security mechanisms than protocols such as WEP by means of handling user authentication and keys more securely. WPA has been further improved by versions such as WPA2 and WPA3.

**SSID:** This is the friendly name of your wireless network that you see when scanning for available networks. It's essentially the network's label.

**ESSID:** While similar to SSID, an ESSID can be associated with multiple access points, often forming a larger network. In the context of Aircrack, it typically refers to the target network you're attempting to attack.

**BSSID:** This is the unique MAC address of an access point. It's like the physical address of your wireless router.

**WPA2-PSK:** This is the most common WiFi security protocol for home and small business networks. It requires a pre-shared key (PSK) that's the same for all devices connecting to the network.

**WPA2-EAP:** This is a more enterprise-grade security protocol that uses a RADIUS server for authentication. It requires users to provide a username and password, which is then verified by the RADIUS server.

**RADIUS:** A RADIUS server is a network access server that authenticates and authorizes users. It's not exclusive to WiFi but is often used in conjunction with WPA2-EAP.

**4-Way Handshake:** This is the core authentication process in WPA and WPA2. It involves a series of messages exchanged between the client and the access point to verify the shared key without revealing it.

**WEP:** A now-deprecated WiFi security protocol that was vulnerable to attacks due to its weak encryption.                                                                                                                                               **Key Derivation:** In WPA and WPA2, the encryption key is derived from both the ESSID and the network password. This makes it more resistant to dictionary attacks.

## **Key Points:**

* **SSID** is the network name.  
* **ESSID** can be associated with multiple access points.  
* **BSSID** is the unique MAC address of an access point.  
* **WPA2-PSK** uses a pre-shared key.  
* **WPA2-EAP** uses a RADIUS server for authentication.  
* **4-Way Handshake** is the core authentication process.  
* **WEP** is an outdated and insecure protocol.

## **Capturing packets to attack**

**Aircrack-ng Suite Components:** The suite includes various tools such as aircrack-ng, airodump-ng, and airmon-ng, which are essential for conducting the attack.

**Setup Requirements:** Users need a Network Interface Card (NIC) that supports monitor mode to capture data packets effectively. Not all wireless cards support this feature.

**Creating a Test Environment:** It is recommended to create a hotspot with a weak password (using passwords from the rockyou.txt wordlist) to practice the attack. A command is provided to generate random passwords from this list.

**Capturing the Handshake:** To crack WPA passwords, capturing the 4-way handshake is crucial. This can be done by forcing a client to reconnect using deauthentication attacks, which can be performed if the NIC supports injection mode.

**Installation:** The Aircrack-ng tools come pre-installed with Kali Linux or can be installed via a package manager or directly from the Aircrack-ng website.

# Cracking Wi-Fi Passwords with Aircrack-ng and Hashcat

To crack the password from a Wi-Fi capture file using Aircrack-ng or Hashcat, follow these instructions and explanations. The process involves using the appropriate flags and tools to efficiently crack the password.

## Instructions

1. **Capture File**: You will need to have a `.cap` file that contains the captured WPA/WPA2 handshake. This file is assumed to be attached.

2. **Using Aircrack-ng**:  
   - To crack the password using Aircrack-ng, use the following command:  
     ```bash  
     aircrack-ng -b 02:1A:11:FF:D9:BD -w /usr/share/wordlists/rockyou.txt capture_file.cap  
     ```  
   - Here, `-b` specifies the BSSID of the target network, and `-w` specifies the wordlist to use for cracking.

3. **Using Hashcat**:  
   - If you prefer to use Hashcat for GPU acceleration, you first need to convert the capture file to HCCAPX format. Use the following command:  
     ```bash  
     hcxpcapngtool -o output.hccapx capture_file.cap  
     ```  
   - Then, crack the password using Hashcat:  
     ```bash  
     hashcat -m 2500 -a 0 output.hccapx /usr/share/wordlists/rockyou.txt  
     ```  
   - In this command, `-m 2500` specifies the hash type for WPA/WPA2, and `-a 0` specifies the attack mode (straight attack).


## Summary  
The process of cracking a Wi-Fi password can be efficiently performed using either Aircrack-ng or Hashcat, with the latter providing faster results when using a GPU. Make sure to use the correct flags to specify the BSSID and wordlist, and convert the capture file to the appropriate format for Hashcat.  

# Linux Buffer Overflow (BOF) & Wireless

## Environment Setup

### Install EDB
Instructions to install the Eclipse Debugger (EDB) on a Linux system.

### Disable ASLR and DEP on Linux
Details on how to disable Address Space Layout Randomization (ASLR) and Data Execution Prevention (DEP) to facilitate buffer overflow testing. This includes modifying system settings and updating the GRUB configuration.

EDB is mentioned as a tool similar to Immunity Debugger, indicating that similar debugging steps can be performed as in a Windows environment.

## GDB Basics Cheat Sheet

### Starting and Quitting
Basic commands to start GDB with a program, run the program, and exit GDB.

### Breakpoints
Commands to set, list, and delete breakpoints within the debugging session.

### Stepping and Continuing
Instructions on how to step through code, either to the next line or into functions, and how to continue program execution.

### Inspecting Variables and Memory
Commands to print the value of expressions, examine memory, and show local variables.

### Stack and Frames
Instructions on how to view the call stack, switch between frames, and get details about the current frame.

### Running and Control
Commands to stop program execution and jump to specific lines or addresses.

### Threads
Commands to list and switch between threads during debugging.

## Exploit Vulnerable Program

### Example Code: `protostar stack5`
A description of a vulnerable C program that contains a buffer overflow vulnerability due to the use of the `gets` function.

### Compile 32-bit Program with No ASLR and No Execution Protection
Instructions for compiling a 32-bit version of the program with specific flags to disable ASLR and execution protection.

## Wireless

### Config Adapter
Information about configuring a specific wireless adapter model (TP-Link TL-WN722N v2/v3) that uses the Realtek RTL8188EUS chipset.

#### Check Adapter Info
Instructions on how to check the status and details of the wireless adapter.

### Install Required Drivers
Details on installing the necessary drivers for the wireless adapter.

### Start Monitoring
Instructions for preparing the wireless adapter for monitoring mode, including checking for conflicting processes and starting the monitoring mode.

### Capture Wireless Packets
Information on how to capture wireless packets to discover available Wi-Fi networks.

### Important Terms
Definitions of key terms related to wireless networking, such as BSSID, ESSID, encryption protocols, and authentication methods.

### Network Power

#### Attacking Target
Instructions on capturing traffic to/from clients to obtain authentication handshakes, including de-authenticating clients to force reconnections.

### Inspecting the Captured Traffic with Wireshark
Instructions on how to analyze captured traffic using Wireshark, specifically filtering for EAPOL packets to find the 4-way handshake.

## Cracking Authentication Keys

### Put the Interface Back to Managed Mode
Instructions for returning the wireless interface to managed mode after monitoring.

### Cracking with Aircrack-ng
Overview of using Aircrack-ng to crack captured handshakes.

### Cracking with Hashcat
Instructions for converting capture files to hash formats and using Hashcat for cracking passwords.

#### Brute Force Attack for 8 Digits
Description of a brute-force attack method specifically targeting 8-digit numeric passwords.

#### Brute Force Attack for 8 Characters (Digits and Alphabet)
Overview of a brute-force attack targeting 8-character passwords that include digits and letters.

#### Brute Force Attack for Lowercase Letters
Description of a brute-force attack focused on lowercase alphabetic characters.

#### Brute Force Attack for 8 to 11 Digits
Instructions for performing a brute-force attack that targets numeric passwords ranging from 8 to 11 digits in length.