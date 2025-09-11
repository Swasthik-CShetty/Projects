# Project 9 — Man-in-the-Middle (MITM) Attack Simulation

**Course / Lab:** Network Security / Ethical Hacking Lab  
**Author:** <Your Name>  
**Date:** <Submission date>  

---

## 1. Introduction
This project demonstrates a **Man-in-the-Middle (MITM)** attack in a controlled lab environment using network security tools such as Ettercap, MITMf, and Wireshark. The purpose is to illustrate how ARP-based MITM techniques can be used to intercept unencrypted traffic, capture sensitive credentials, and study defensive mechanisms. The simulation was performed only on isolated virtual machines, ensuring ethical and safe experimentation.

---

## 2. Abstract
This project simulates an ARP spoofing-based MITM attack within a VM lab setup. By positioning the attacker between a victim machine and the gateway, traffic was intercepted and analyzed. The captured data revealed that plaintext HTTP traffic exposes sensitive information, while HTTPS traffic remained secure. The experiment highlights the critical role of encryption (HTTPS, HSTS) and network defenses (ARP protection, IDS/IPS) in mitigating MITM attacks. The project reinforces the importance of ethical hacking practices and defense-in-depth strategies.

---

## 3. Tools Used
- **Host OS:** <Your Host OS, e.g., Ubuntu 24.04 LTS>  
- **Virtualization:** VirtualBox / VMware Workstation (bridged network mode)  
- **Attacker VM:** Kali Linux — Tools: Ettercap, MITMf, tcpdump  
- **Victim VM:** Ubuntu / Windows with a vulnerable HTTP test web app (e.g., DVWA or custom login form)  
- **Analysis Tool:** Wireshark  
- **Other Resources:** OWASP documentation, RFC 826 (ARP), tool manuals  

---

## 4. Steps Involved in Building the Project

### 4.1 Lab Preparation
1. Created two VMs (`attacker` and `victim`) in bridged networking mode.  
2. Configured a test web application on the victim that accepts HTTP logins.  
3. Installed Wireshark and confirmed VM connectivity.  

### 4.2 Attack / Data Collection
4. The attacker launched ARP spoofing using Ettercap/MITMf to redirect victim traffic through the attacker.  
5. The victim attempted a login on the HTTP web app using test credentials.  
6. Traffic was captured and saved to a `.pcap` file.  

### 4.3 Analysis
7. Wireshark was used to analyze the captured traffic. HTTP POST requests showed credentials in plaintext.  
8. A comparison with HTTPS logins confirmed that credentials were not visible due to encryption.  

### 4.4 Remediation & Cleanup
9. The MITM process was stopped, ARP caches cleared, and systems restored to normal.  
10. Defensive measures were reviewed and documented.  

---

## 5. Screenshots / Outputs

### Ettercap Host Scanning
![Ettercap Host Scan](Screenshot%202025-09-11%20231538.png)

### Ettercap MITM Menu (ARP Poisoning)
![Ettercap ARP Poisoning Menu](Screenshot%202025-09-11%20231550.png)

### ARP Poisoning Options Dialog
![Ettercap ARP Options](Screenshot%202025-09-11%20231604.png)

### Wireshark Capture of ICMP Packets
![Wireshark ICMP Capture](Screenshot%202025-09-11%20231628.png)

### ARP Table Showing Poisoned Entries
![ARP Table Result](Screenshot%202025-09-11%20231648.png)

**Sample redacted HTTP POST request:**
```
POST /login HTTP/1.1
Host: victim.local
Content-Type: application/x-www-form-urlencoded
Content-Length: 42

username=testuser&password=[REDACTED]
```

---

## 6. Conclusion
The project successfully demonstrated a MITM attack using ARP spoofing in a controlled environment. It showed how attackers can harvest sensitive information from unencrypted HTTP traffic, while HTTPS secured the communication. The exercise highlighted the importance of enforcing encrypted communication, implementing ARP protection, and monitoring with IDS/IPS. It also reinforced the ethical responsibility to only conduct such experiments in isolated, authorized environments.

---

## 7. Challenges Faced
- Ensuring proper VM isolation in bridged network mode.  
- Installing and configuring MITMf dependencies.  
- Interpreting and filtering Wireshark packet data for relevant credentials.  

---

## 8. References
1. Ettercap Project Documentation – [https://www.ettercap-project.org](https://www.ettercap-project.org)  
2. MITMf GitHub Repository – [https://github.com/byt3bl33d3r/MITMf](https://github.com/byt3bl33d3r/MITMf)  
3. Wireshark User Guide – [https://www.wireshark.org/docs/](https://www.wireshark.org/docs/)  
4. OWASP Testing Guide – “Man-in-the-Middle Attack”  
5. RFC 826 — Address Resolution Protocol (ARP)  

---

## Appendix
- **Appendix A:** VM configurations (RAM, CPU, NIC type, IPs).  
- **Appendix B:** Capture metadata (pcap filename, size, packet count).  
- **Appendix C:** Redacted packet extracts.  
- **Appendix D:** Sample IDS/IPS ARP spoofing detection rules.  
