# Task 09 – Man-in-the-Middle (MITM) Attack using Ettercap / MITMf

## Objective
To understand how a **Man-in-the-Middle (MITM)** attack works on a local network by performing **ARP spoofing** to intercept and monitor traffic between two devices.  
This task demonstrates the importance of encryption and secure communication protocols.

---
## Tools Used
- **Kali Linux** 
- **Ettercap** 
- **Wireshark** 
---
## ⚙️ Steps Performed

### 1. Environment Setup
- Configured a virtual lab with two machines:
  - **Attacker** → Kali Linux
  - **Victim** → old phone

### 2. Tool Installation
On Kali, installed Ettercap:
sudo apt update
sudo apt install ettercap-graphical

### 3. Enabled IP Forwarding
This allowed packets to flow through the attacker without breaking the victim’s connection
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

### 4. Launched Ettercap
sudo ettercap -G
Selected Unified Sniffing on the active network interface.
Scanned for hosts in the LAN.
Identified the Victim and Gateway IP addresses.
Added Victim as Target 1 and Gateway as Target 2.


