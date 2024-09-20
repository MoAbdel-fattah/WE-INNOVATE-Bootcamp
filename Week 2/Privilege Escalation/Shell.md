# **Shell**

- what we use when interfacing with a Command Line environment (CLI)  
- the common bash or sh programs in Linux.  
- cmd.exe and Powershell on Windows.  
- **Reverse shell:** remote server to either send us command line access to the server.  
- **Bind shell:** open up a port on the server which we can connect to in order to execute further commands.

## **Reverse shell**

- execute code that connects *back* to your computer.  
- Use listener which would be used to receive the connection.  
- good way to bypass firewall rules.

### **Staged vs. Stageless Reverse Shell Payloads**

####  **Staged Payloads:**  
  * Sent in two parts: a stager and the main payload.  
  * Stager executes on the target, connects to a listener, and downloads the main payload.  
  * Avoids disk contact, reducing detection by antivirus.  
  * Requires a specialized listener like Metasploit's multi/handler.  
#### **Stageless Payloads:**  
  * Entirely self-contained in a single piece of code.  
  * Executes and sends a shell back immediately to the listener.  
  * More common and simpler to use.

## **Blind shell**

- The code executed on the target is used to start a listener attached to a shell directly on the target.  
- Opened up to the internet  
- Can connect to the port that the code has opened and obtain **remote code execution(RCE**) that way.   
- May be prevented by firewalls protecting the target.

## **Webshells: A Gateway to Server Control**

**Webshells** are malicious scripts, typically written in languages like PHP, ASP, or Perl, that are designed to run within a web server. These scripts act as backdoors, providing attackers with unauthorized access to the server's underlying operating system and files.

### **How Webshells Work**

1. **Installation:** Webshells are often uploaded to a compromised website, either through vulnerabilities in the web application or by exploiting misconfigurations.  
2. **Execution:** When a user visits a specific URL or triggers a certain action, the webshell is executed.  
3. **Command Execution:** The webshell allows the attacker to execute commands on the server, granting them control over the system's resources.

### **Common Uses of Webshells**

* **Data Exfiltration:** Attackers can use webshells to steal sensitive data, such as credit card numbers, customer information, or intellectual property.  
* **Lateral Movement:** Webshells can be used as a foothold to gain access to other systems within a network.  
* **Persistence:** Attackers can use webshells to maintain persistent access to a compromised system, even after initial intrusion.  
* **Denial of Service (DoS):** Webshells can be used to launch DoS attacks against other systems or websites.

### **Detecting and Preventing Webshells**

* **Regular Security Audits:** Conduct regular security audits to identify vulnerabilities that could be exploited to install webshells.  
* **Web Application Firewalls (WAFs):** Use WAFs to detect and block malicious web requests, including those that attempt to upload webshells.  
* **Intrusion Detection Systems (IDS):** Implement IDS solutions to monitor network traffic for suspicious activity, such as the execution of webshells.  
* **Regular Patching:** Keep web servers and applications up-to-date with the latest security patches to address known vulnerabilities.  
* **User Education:** Train users to be aware of the risks of clicking on suspicious links or downloading attachments from unknown sources.

## **Ok, we have a shell. Now what?**

* **Linux:** Look for SSH keys in `/home/<user>/.ssh`, credentials in system files, or exploit vulnerabilities like Dirty C0w to gain SSH access.  
* **Windows:** Search for passwords in the registry, especially for services like VNC or FileZilla. Aim for SYSTEM or administrator privileges to add your own account and use RDP, telnet, or other methods for remote access.  
* **Best Practice:** Always strive to escalate to a "normal" access method for easier exploitation of the target.