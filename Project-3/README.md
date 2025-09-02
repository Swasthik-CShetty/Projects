# 🛰️ Project 3: Network Packet Sniffer

## 📌 Objective
The goal of this project is to build a **Python-based network packet sniffer** using **Scapy**.  
The sniffer captures live packets, analyzes headers, extracts key details (IP, ports, payload), and logs the results with timestamps.

---

## ⚙️ Tools & Technologies
- **Python 3**
- **Scapy** (packet crafting and sniffing library)
- **Kali Linux** (for root access and network monitoring)

---

## 🔹 Features
- Captures live packets from a chosen network interface  
- Filters traffic (e.g., TCP, HTTP, FTP, UDP)  
- Extracts key header fields:
  - Source IP
  - Destination IP
  - Protocol
  - Source/Destination Ports
  - Payload (if available)  
- Saves logs to a file with timestamps (`packet_logs.txt`)  

---

