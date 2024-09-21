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