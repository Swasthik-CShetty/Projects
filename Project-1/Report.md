# **Project 1: Vulnerability Scanning on Localhost Web App**

---

## **1. Introduction**

This project focuses on identifying vulnerabilities in a local web application using automated scanning tools and manual analysis. The goal is to understand common security flaws in web apps and practice real-world penetration testing techniques in a controlled environment.

---

## **2. Abstract**

The project demonstrates scanning a web application (e.g., DVWA or BWAPP) to detect security vulnerabilities such as SQL injection, XSS, CSRF, and directory traversal. Tools like **Nmap**, **Nikto**, and **OWASP ZAP** are used to identify issues. Alerts and reports generated provide insights into potential threats, which can then be mitigated.

---

## **3. Tools Used**

* **Operating System**: Kali Linux
* **Vulnerable Web App**: DVWA or BWAPP installed on XAMPP/LAMP stack
* **Tools**:

  * `Nmap` → Network scanning and open ports
  * `Nikto` → Web server vulnerability scanning
  * `OWASP ZAP` → Intercepting and analyzing web traffic
* **Browser**: Chrome/Firefox (with proxy for OWASP ZAP)

---

## **4. Steps Involved in Building the Project**

### **Step 1: Set up Local Web App**

* Install DVWA.
* Configure MySQL database and create default users.

### **Step 2: Run Network Scans**

* Identify open ports and services using Nmap:

nmap -sV localhost

### **Step 3: Scan for Web Vulnerabilities**

* Run Nikto on the web app:

nikto -h http://localhost/dvwa

* Analyze output for known vulnerabilities.

### **Step 4: Intercept Traffic with OWASP ZAP**

* Configure browser to use ZAP proxy.
* Perform web actions (login, form submissions) to see requests/responses in ZAP.
* Identify issues like XSS, CSRF, and insecure cookies.



## **5.Outputs**

* **Nmap Scan Results** → Ports and services detected
* **Nikto Scan Output** → Vulnerabilities and warnings
* **OWASP ZAP Alerts** → XSS, CSRF, cookie security issues


---

## **6. Conclusion**

The project successfully demonstrates how automated tools can help identify vulnerabilities in web applications. By combining Nmap, Nikto, and OWASP ZAP, both network-level and application-level weaknesses were identified. This exercise improved understanding of common web security flaws and the importance of regular vulnerability scanning.

---

## **7. Challenges Faced**

* Configuring DVWA/BWAPP correctly on Kali/Linux
* Setting up OWASP ZAP proxy with browser
* Handling false positives in automated scans

---
