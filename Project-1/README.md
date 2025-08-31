# Project 1: Vulnerability Scanning on a Localhost Web Application

## Overview
This project focuses on identifying and analyzing security vulnerabilities in a deliberately vulnerable web application called **DVWA (Damn Vulnerable Web Application)**, hosted locally. The goal is to understand potential security flaws and how they can be mitigated, providing hands-on experience in vulnerability scanning and web security.
---
## Tools Used
- **DVWA** – a PHP/MySQL web app intentionally designed to be insecure.  
- **XAMPP** – a local web server environment to run DVWA.  
- **Nikto** – a web server scanner for detecting common vulnerabilities.  
- **Nmap** – a network scanning tool to discover open ports and services.  
- **OWASP ZAP** – a penetration testing tool for web application vulnerabilities.
---
## Steps Taken
### 1. Setting Up DVWA
1. Installed **XAMPP** and started the **Apache** and **MySQL** services.  
2. Downloaded DVWA and placed it in the XAMPP `htdocs` folder.  
3. Configured the database using DVWA’s `setup.php` script.  
4. Logged in with the default credentials:
   - **Username:** `admin`  
   - **Password:** `password`  
---
### 2. Scanning the Application
#### Nikto Scan
Nikto was used to check for common web server vulnerabilities:
nikto -h http://localhost/dvwa
#### 3.Nmap Scan
Nmap was used to identify open ports and detect vulnerabilities:
nmap -sV -A localhost
nmap --script vuln -p 80,3306 localhost
#### 4.Web Application Analysis with OWASP ZAP
OWASP ZAP was configured as a proxy to intercept DVWA traffic.
The website was spidered to map all pages and parameters.
An active scan identified vulnerabilities such as:
SQL Injection (SQLi)
Cross-Site Scripting (XSS)
Cross-Site Request Forgery (CSRF)
A detailed HTML report was generated for documentation.
##Conclusion
The project provides practical experience in assessing web application security. Tools like Nikto, Nmap, and OWASP ZAP help identify vulnerabilities, understand their impact, and suggest mitigation techniques. This knowledge forms a foundation for penetration testing and web security practices.






