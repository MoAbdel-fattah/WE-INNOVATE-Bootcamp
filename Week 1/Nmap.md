Nmap

\- when you connect to numerous websites at the same time.   
Your computer opens up a different, high-numbered port (at random), which it uses for all its communications with the remote server.

\- Every computer has a total of 65535 available ports  
\- A HTTPS Webservice can be found on port 443  
\- Windows NETBIOS can be found on port 139

* NetBIOS is an acronym for Network Basic Input/Output System. It provides services related to the session layer of the OSI model allowing applications on separate computers to communicate over a local area network.

\- SMB can be found on port 445\.

* Server Message Block (SMB) is a communication protocol\[1\] originally developed in 1983 by Barry A. Feigenbaum at IBM\[2\] and intended to provide shared access to files and printers across nodes on a network of systems running IBM's OS/2. It also provides an authenticated inter-process communication (IPC) mechanism.

## **Syn Scan in Nmap: A Closer Look**

**Syn Scan** is a popular technique used in network scanning, particularly with the Nmap tool. It's designed to identify live hosts on a network without fully establishing a connection. This approach minimizes the risk of triggering intrusion detection systems (IDS) and firewalls.

- **Intrusion Detection Systems (IDS)** are security tools designed to monitor network traffic and system activity for signs of unauthorized access or malicious behavior.

### **How Syn Scan Works**

1. **Packet Construction:** Nmap crafts a TCP SYN packet, essentially a request to initiate a connection. This packet includes the destination IP address and a random source port number.  
2. **Transmission:** The SYN packet is sent to the target host.  
3. **Response Analysis:** The target host responds to the SYN packet with one of three possible responses:  
   * **SYN/ACK:** This indicates that the host is alive and willing to establish a connection.  
   * **RST:** This means the host is alive but refuses the connection.  
   * **No response:** If there's no response, the host is likely either offline or has dropped the packet.  
4. **Connection Reset:** Nmap immediately sends a RST packet to terminate the connection, preventing a full three-way handshake.

### **Advantages of Syn Scan**

* **Stealth:** By only sending a SYN packet, Syn Scan minimizes the risk of detection by IDS and firewalls.  
* **Efficiency:** It's relatively fast compared to other scan types as it doesn't require a full connection.  
* **Versatility:** Syn Scan can be used to identify live hosts, detect open ports, and gather basic information about services running on those ports.

### **Limitations of Syn Scan**

* **False Positives:** In some cases, firewalls or network devices might drop SYN packets without a response, leading to false negatives.  
* **Detection:** While stealthier than other scans, Syn Scan can still be detected by advanced IDS systems that monitor network traffic patterns.  
* **Limited Information:** Syn Scan provides basic information about host availability and open ports but doesn't reveal detailed service information.

## **UDP and UDP Scan in Nmap**

**UDP (User Datagram Protocol)** is a connectionless transport layer protocol used in the TCP/IP model. Unlike TCP, UDP does not guarantee delivery or ordering of packets, making it less reliable but more efficient for certain applications.

**UDP Scan** in Nmap is a technique used to identify open UDP ports on a target host. Unlike TCP scans, UDP scans don't establish a connection, making them potentially less detectable by firewalls and intrusion detection systems.

### **How UDP Scan Works**

1. **Packet Construction:** Nmap crafts a UDP datagram with a destination port number.  
2. **Transmission:** The datagram is sent to the target host.  
3. **Response Analysis:** If the target host responds with a UDP datagram, it indicates that the port is open. If there's no response, the port is likely closed or filtered.

### **Advantages of UDP Scan**

* **Speed:** UDP scans are generally faster than TCP scans as they don't require a three-way handshake.  
* **Stealth:** Due to their connectionless nature, UDP scans can sometimes bypass firewalls and intrusion detection systems.

### **Limitations of UDP Scan**

* **Reliability:** UDP doesn't guarantee delivery, so there's a chance that a response might be lost, leading to false negatives.  
* **Filtering:** Some firewalls and network devices might block UDP traffic, making it difficult to accurately determine the status of UDP ports.


  

## **Operating System Scan in Nmap**

The `-O` option in Nmap is used to perform **operating system detection**. It attempts to identify the operating system of a target host based on the responses to various probes sent during a scan.

**How it works:**

1. **Probe Selection:** Nmap sends a series of carefully crafted probes to the target host. These probes can include TCP SYN packets, UDP packets, ICMP packets, or other specific payloads.  
2. **Response Analysis:** Nmap analyzes the responses to these probes, looking for patterns that are characteristic of specific operating systems. These patterns can include things like the version number of the TCP stack, the behavior of certain services, or the specific flags set in response packets.  
3. **Operating System Identification:** Based on the observed patterns, Nmap attempts to match the responses to known signatures of different operating systems. If a match is found, Nmap reports the identified operating system.

**Factors Affecting Accuracy:**

* **Firewall Rules:** Firewalls can interfere with Nmap's ability to detect the operating system by blocking or modifying probes.  
* **Operating System Configuration:** Custom configurations or security hardening can make it more difficult to accurately identify the operating system.  
* **Nmap's Database:** The accuracy of Nmap's operating system detection depends on the completeness and accuracy of its internal database of known operating system signatures.

## **Service Scan in Nmap**

The `-sV` option in Nmap is used to perform **service version detection**. It attempts to identify the versions of services running on open ports of a target host.

**How it works:**

1. **Service Detection:** Nmap first identifies open ports on the target host using other scan types, such as `-sS` for SYN scan or `-sU` for UDP scan.  
2. **Probe Selection:** Nmap then sends specific probes to each open port, designed to elicit responses that can be used to identify the service and its version. These probes can include sending specific requests, analyzing the banner information returned by the service, or interacting with the service's protocol.  
3. **Version Identification:** Nmap analyzes the responses to these probes, looking for patterns that are characteristic of specific service versions. These patterns can include things like the version number included in the service's banner, the specific responses to certain requests, or the behavior of the service under different conditions.  
4. **Version Reporting:** If Nmap is able to identify the service and its version, it reports this information along with other details about the port and the host.

**Factors Affecting Accuracy:**

* **Service Configuration:** Custom configurations or security hardening can make it more difficult to accurately identify the service version.  
* **Service Behavior:** Some services may not provide enough information in their responses to allow for accurate version detection.  
* **Nmap's Database:** The accuracy of Nmap's service version detection depends on the completeness and accuracy of its internal database of known service signatures.

**Verbosity level of the scan**

The `-v` option in Nmap is used to increase the **verbosity level** of the scan. This means that Nmap will provide more detailed output, including additional information about the scan process, the results, and any errors or warnings that occur.                                                                                     **Key points about the `-v` option:**

* **Increased detail:** The more `-v` options you use, the more detailed the output will be. For example, using `-vv` will provide more information than using `-v`, and using `-vvv` will provide even more.  
* **Progress updates:** Nmap will provide regular updates on the progress of the scan, including the number of hosts scanned, the number of ports checked, and the estimated time remaining.  
* **Error and warning messages:** Nmap will display more detailed error and warning messages if any issues arise during the scan.  
* **Debugging information:** For advanced users, using multiple `-v` options can provide debugging information that can be helpful in troubleshooting issues.

**Nmap Output Formats: \-oN, \-oX, \-oS, \-oG, and \-oA**

Nmap provides various output formats to suit different needs and preferences. These formats allow you to save the scan results for later analysis, sharing, or integration with other tools.

### **\-oN \<file\>**

* **Normal format:** This is the default output format and provides a human-readable, tabular representation of the scan results. It includes information about hosts, ports, services, and other relevant details.

### **\-oX \<file\>**

* **XML format:** This format saves the scan results in XML, a structured data format that can be easily parsed and processed by other applications. XML output is ideal for integrating Nmap results with other tools or for automated analysis.

### **\-oS \<file\>**

* **Script Kiddie format:** This format is designed to be easily readable by individuals who may not have a deep understanding of networking or security. It provides a simplified version of the scan results, focusing on the most relevant information.

### **\-oG \<file\>**

* **Grepable format:** This format is optimized for searching and filtering using the `grep` command. It outputs the results in a format that is easy to parse and search for specific patterns.

### **\-oA \<basename\>**

* **All formats:** This option saves the scan results in all three major formats at once, using a common base filename and adding appropriate extensions

## **Stealth Scans: TCP Null, FIN, and Xmas Scans**

Nmap offers several stealth scan techniques designed to minimize detection by firewalls and intrusion detection systems (IDS). These techniques involve sending specially crafted TCP packets that are less likely to trigger alarms.

### **TCP Null Scans (-sN)**

* **Description:** In a TCP Null scan, Nmap sends a TCP packet with all flags set to zero. This type of packet is often ignored or dropped by firewalls, as it doesn't represent a valid connection attempt.  
* **Purpose:** To identify open ports while minimizing detection.

### **TCP FIN Scans (-sF)**

* **Description:** In a TCP FIN scan, Nmap sends a TCP packet with only the FIN flag set. This flag is typically used to terminate a connection, but when sent to an open port without an existing connection, it may elicit a response.  
- The FIN (Finish) flag is a control flag used in the Transmission Control Protocol (TCP) to indicate that a sender has no more data to send and is terminating the connection.  
* **Purpose:** To identify open ports, similar to TCP Null scans.

### **TCP Xmas Scans (-sX)**

* **Description:** In a TCP Xmas scan, Nmap sends a TCP packet with the FIN, SYN, and ACK flags set. This combination of flags is considered unusual and may trigger a response from certain firewalls or servers.  
* **Purpose:** To identify open ports, but with a slightly higher risk of detection compared to Null and FIN scans.

**Key Points:**

* These stealth scan techniques are designed to avoid triggering alarms on firewalls and IDS.  
* They are often used to identify open ports on systems that might be protected by security measures.  
* The effectiveness of these scans can vary depending on the specific firewall rules and IDS configurations.  
* It's essential to use these scans responsibly and ethically, adhering to applicable laws and regulations.

## **TCP Connect Scans**

In TCP, several flags are used to control the flow of data and establish connections. When a client sends a SYN packet to initiate a connection, the server's response will include one or more of these flags to indicate its status.

### **Common Response Flags:**

* **SYN-ACK:** This flag combination is sent by the server to acknowledge the client's SYN packet and initiate its own connection. It indicates that the server is willing to establish a connection.  
* **RST:** If the server refuses the connection, it will send a RST (Reset) flag. This indicates that the connection is terminated immediately.  
* **ACK:** This flag is used to acknowledge the receipt of data. It is often combined with other flags, such as SYN-ACK or FIN.  
* **FIN:** This flag indicates that the sender has no more data to send and is terminating the connection.

**Additional Response Flags:**

* **URG:** This flag indicates that the data following the URG flag should be treated as urgent.  
* **PSH:** This flag urges the receiver to deliver data immediately, rather than buffering it.  
* **ECE:** This flag indicates that the sender experienced congestion on the path to the receiver.  
* **CWR:** This flag indicates that the receiver has reduced its window size due to congestion.

**Understanding Response Flags:**

By analyzing the flags in a server's response, you can determine the status of the connection and identify potential issues. For example:

* **SYN-ACK:** The server is willing to establish a connection.  
* **RST:** The server refused the connection, possibly due to a closed port or security policy.  
* **FIN:** The server is terminating the connection.  
* **Other flags:** These flags may indicate congestion, prioritization, or other network-related conditions.

**Using Response Flags:**

Understanding response flags is essential for network troubleshooting and security analysis. By analyzing the flags in TCP packets, you can identify problems, diagnose issues, and take appropriate actions to resolve them.

## **SYN Connect Scans**

**SYN Scans** are a popular technique used in network scanning, particularly with the Nmap tool. They're designed to identify live hosts on a network without fully establishing a connection. This approach minimizes the risk of triggering intrusion detection systems (IDS) and firewalls.

### **How SYN Scans Work**

1. **Packet Construction:** Nmap crafts a TCP SYN packet, essentially a request to initiate a connection. This packet includes the destination IP address and a random source port number.  
2. **Transmission:** The SYN packet is sent to the target host.  
3. **Response Analysis:** The target host responds to the SYN packet with one of three possible responses:  
   * **SYN/ACK:** This indicates that the host is alive and willing to establish a connection.  
   * **RST:** This means the host is alive but refuses the connection.  
   * **No response:** If there's no response, the host is likely either offline or has dropped the packet.  
4. **Connection Reset:** Nmap immediately sends a RST packet to terminate the connection, preventing a full three-way handshake.

**Common Response Flags:**

* **SYN-ACK:** This flag combination is sent by the server to acknowledge the client's SYN packet and initiate its own connection. It indicates that the server is willing to establish a connection.  
* **RST:** If the server refuses the connection, it will send a RST (Reset) flag. This indicates that the connection is terminated immediately.  
* **ACK:** This flag is used to acknowledge the receipt of data. It is often combined with other flags, such as SYN-ACK or FIN.  
* **FIN:** This flag indicates that the sender has no more data to send and is terminating the connection.

**Understanding Response Flags:**

By analyzing the flags in a server's response, you can determine the status of the connection and identify potential issues. For example:

* **SYN-ACK:** The server is willing to establish a connection.  
* **RST:** The server refused the connection, possibly due to a closed port or security policy.  
* **FIN:** The server is terminating the connection.  
* **Other flags:** These flags may indicate congestion, prioritization, or other network-related conditions.

  ### **Common Firewall Evasion Techniques**

* **Port Scanning:** Identifying open ports on a target system can reveal potential vulnerabilities that can be exploited.  
* **Protocol Spoofing:** Disguising the source or destination IP address or protocol to bypass firewall rules.  
* **Fragmentation:** Dividing data into smaller fragments to evade firewall rules that inspect entire packets.  
* **Encryption:** Encrypting data to hide its contents from firewalls that inspect cleartext traffic.  
* **Stealth Scans:** Using scan techniques like TCP Null, FIN, or Xmas scans to minimize detection.  
* **Application-Layer Attacks:** Exploiting vulnerabilities in specific applications or protocols that bypass firewall controls.  
* **Protocol Abuse:** Misusing or abusing legitimate protocols to bypass firewall rules.  
* **Tunneling:** Encapsulating data within another protocol to bypass firewall filters.  
* **Social Engineering:** Manipulating users into bypassing security controls or providing sensitive information.

  ### **Mitigating Firewall Evasion**

To counter firewall evasion techniques, organizations can implement the following measures:

* **Comprehensive Firewall Rules:** Create robust firewall rules to block unauthorized traffic and prevent known vulnerabilities from being exploited.  
* **Regular Updates:** Keep firewall software and signatures up-to-date to address new threats.  
* **IDS/IPS:** Deploy intrusion detection and prevention systems to monitor network traffic for suspicious activity and take action to block attacks.  
* **Network Segmentation:** Divide the network into smaller segments to limit the spread of attacks.  
* **User Education:** Educate users about security best practices and the risks of clicking on suspicious links or downloading attachments from unknown sources.  
* **Regular Vulnerability Assessments:** Conduct regular vulnerability assessments to identify and address weaknesses in the network infrastructure.  
* **Threat Intelligence:** Stay informed about emerging threats and trends to adapt security measures accordingly.

**Microsoft Windows is one of the common operating systems that may respond to a NULL, FIN, or Xmas scan with a RST for every port.**

This behavior is due to the way Windows handles these types of scans. When Windows receives a TCP packet with a NULL, FIN, or Xmas flag, it often interprets it as an invalid or malicious attempt to connect. As a security measure, it responds with a RST packet to terminate the connection immediately.

This response can make it more difficult to identify open ports on Windows systems using these stealth scan techniques. However, it's important to note that this behavior may vary depending on the specific Windows version, configuration, and network settings.

**NSE Scripts**

The Nmap Scripting Engine (NSE) is a powerful tool that allows you to extend Nmap's capabilities by writing custom scripts. These scripts can perform a wide range of tasks, such as:

* **Identifying services:** Determining the specific version of a service running on a port.  
* **Checking for vulnerabilities:** Scanning for known vulnerabilities in services or applications.  
* **Gathering additional information:** Collecting data about a system, such as its operating system or configuration.  
* **Interacting with services:** Sending custom requests to services and analyzing their responses.

**Key features of NSE:**

* **Scripting language:** NSE uses Lua, a lightweight and efficient programming language.  
* **Integration with Nmap:** Scripts can be easily integrated into Nmap scans using the `-sC` option.  
* **Large script library:** Nmap comes with a built-in library of scripts that can be used for various tasks.  
* **Custom script development:** You can write your own scripts to meet specific needs.


