# **Linux Privilege Escalation**

- Privilege Escalation usually involves going from a lower permission account to a higher permission one. More technically, it's the exploitation of a vulnerability, design flaw, or configuration oversight in an operating system or application to gain unauthorized access to resources that are usually restricted from the users.


## **Why is it important?**

* Resetting passwords  
* Bypassing access controls to compromise protected data  
* Editing software configurations  
* Enabling persistence  
* Changing the privilege of existing (or new) users  
* Execute any administrative command

### **Common Techniques**

#### **1\. Exploiting System Vulnerabilities:**

* **Sudo Misconfigurations:** Incorrectly configured `sudoers` files can grant excessive privileges.  
* **Setuid/Setgid Programs:** Programs that run with elevated privileges can be exploited if they have vulnerabilities.  
* **Kernel Vulnerabilities:** Exploiting vulnerabilities in the Linux kernel can lead to privilege escalation.

#### **2\. Password Cracking and Credential Theft:**

* **Password Cracking:** Using brute force or dictionary attacks to guess passwords.  
* **Credential Theft:** Stealing credentials from files, memory, or through phishing attacks.

#### **3\. Weak Configurations:**

* **Default Credentials:** Using default usernames and passwords.  
* **Misconfigured Services:** Services running with excessive privileges.  
* **Weak Permissions:** Files or directories with incorrect permissions.

#### **4\. Lateral Movement:**

* **Pass-the-Hash:** Using a stolen hash to authenticate to other systems.  
* **Token Stealing:** Capturing a user's authentication token to impersonate them.

## **Real-World Examples**

* **Sudo Vulnerability:** The `sudo` command can be exploited if a user can execute a command with `sudo` that has a vulnerability.  
* **Dirty Cow:** A vulnerability that allowed an attacker to write to arbitrary memory locations, potentially leading to privilege escalation.  
* **Ghost Shell:** A vulnerability in the `bash` shell that could be exploited to execute arbitrary code.

## **Mitigation Strategies**

* **Regular Patching:** Keep systems up-to-date with the latest security patches.  
* **Strong Password Policies:** Enforce strong, unique passwords.  
* **Least Privilege Principle:** Grant users only the minimum necessary privileges.  
* **Regular Security Audits:** Conduct regular security assessments to identify vulnerabilities.  
* **Security Awareness Training:** Educate users about security best practices.  
* **Hardening Systems:** Implement security hardening measures to reduce the attack surface.

## **Additional Considerations**

* **Privilege Escalation Tools:** Several tools, such as `sudo`, `su`, and `pwnkit`, can be used to elevate privileges.  
* **Privilege Escalation Frameworks:** Frameworks like Metasploit and Cobalt Strike provide automated tools for privilege escalation.  
* **Ethical Hacking:** Privilege escalation is a common technique used in ethical hacking to test the security of systems.


## **Detailed Example: Sudo Misconfiguration**

A common privilege escalation technique involves misconfiguring the `sudoers` file, which controls which users can execute commands with elevated privileges. For example, if a user is allowed to run `sudo -i`, they can gain root privileges.

**Example `sudoers` file:**
```
root    ALL=(ALL:ALL) ALL  
user    ALL=ALL
```
In this example, the `user` can run any command with `sudo`. This could be exploited by an attacker who has compromised the `user` account to gain root privileges.

To prevent this, the `sudoers` file should be carefully configured to grant only the necessary privileges. For example, the following configuration would allow the `user` to run only specific commands:
```
root    ALL=(ALL:ALL) ALL  
user    ALL=(ALL:ALL) /usr/bin/systemctl, /usr/bin/service
```
