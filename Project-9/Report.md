# Project 9 — Man-in-the-Middle (MITM) Attack Simulation  

---

## 1. Introduction
This project demonstrates a **Man-in-the-Middle (MITM)** attack in a controlled lab environment using network security tools such as Ettercap, MITMf, and Wireshark. The purpose is to illustrate how ARP-based MITM techniques can be used to intercept unencrypted traffic, capture sensitive credentials, and study defensive mechanisms. The simulation was performed only on isolated virtual machines, ensuring ethical and safe experimentation.

---

## 2. Abstract
This project simulates an ARP spoofing-based MITM attack within a VM lab setup. By positioning the attacker between a victim machine and the gateway, traffic was intercepted and analyzed. The captured data revealed that plaintext HTTP traffic exposes sensitive information, while HTTPS traffic remained secure. The experiment highlights the critical role of encryption (HTTPS, HSTS) and network defenses (ARP protection, IDS/IPS) in mitigating MITM attacks. The project reinforces the importance of ethical hacking practices and defense-in-depth strategies.

---

## 3. Tools Used
- **Host OS:** <Host OS, e.g., Ubuntu 24.04 LTS>  
- **Virtualization:** VMware Workstation (bridged network mode)  
- **Attacker VM:** Kali Linux — Tools: Ettercap, MITMf, tcpdump  
- **Victim VM:** Ubuntu with a vulnerable HTTP test web app 
- **Analysis Tool:** Wireshark  

---

## 4. Steps Involved in Building the Project

### 4.1 Lab Preparation
1. Created two VMs (`attacker` and `victim`) in bridged networking mode.  
2. Configured a test web application on the victim that accepts HTTP logins.  
3. Installed Wireshark and confirmed VM connectivity.  

### 4.2 Attack / Data Collection
4. The attacker launched ARP spoofing using Ettercap/MITMf to redirect victim traffic through the attacker.  
5. The victim attempted a login on the HTTP web app using test credentials.  
6. Traffic was captured.  

### 4.3 Analysis
7. Wireshark was used to analyze the captured traffic. HTTP POST requests showed credentials in plaintext.  
8. A comparison with HTTPS logins confirmed that credentials were not visible due to encryption.  

### 4.4 Remediation & Cleanup
9. The MITM process was stopped, ARP caches cleared, and systems restored to normal.  
10. Defensive measures were reviewed and documented.  

---

## 5. Screenshots / Outputs

### Ettercap Host Scanning
![Ettercap Host Scan](<img width="857" height="542" alt="Screenshot 2025-09-11 231538" src="https://github.com/user-attachments/assets/b964b4fc-58ca-44c7-be9b-5045096183e1" />)


### Ettercap MITM Menu (ARP Poisoning)
![Ettercap ARP Poisoning Menu](<img width="745" height="491" alt="Screenshot 2025-09-11 231550" src="https://github.com/user-attachments/assets/0d8ae416-265b-4363-9f9e-34bb14405332" />)

### ARP Poisoning Options Dialog
![Ettercap ARP Options](<img width="812" height="508" alt="Screenshot 2025-09-11 231604" src="https://github.com/user-attachments/assets/5ef0d32b-9323-4f95-a6ea-3360c9267c84" />
)

### Wireshark Capture of ICMP Packets
![Wireshark ICMP Capture](<img width="874" height="649" alt="Screenshot 2025-09-11 231628" src="https://github.com/user-attachments/assets/c27e73e8-15dd-4f66-826b-f71675b75360" />
)

### ARP Table Showing Poisoned Entries
![ARP Table Result](<img width="847" height="351" alt="Screenshot 2025-09-11 231648" src="https://github.com/user-attachments/assets/dfee6dd5-8376-435d-92e7-571c67db3cff" />
)

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
1. Ettercap Project   
2. Wireshark
3. YouTube   

--- 
