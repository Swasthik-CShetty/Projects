Project 6: Firewall Rules Using UFW/iptables
1. Introduction

Firewalls are essential for protecting systems by controlling incoming and outgoing network traffic. This project demonstrates how to configure a firewall on a Linux VM to allow only specific services (SSH and HTTP) while blocking all other traffic. The project also simulates blocked ping requests and port scans to verify the firewall’s effectiveness.

2. Objective

Configure firewall rules using UFW or iptables.

Allow only SSH (port 22) and HTTP (port 80).

Block all other traffic.

Simulate and verify blocked ping and port scans.

3. Tools Used

Operating System: Kali Linux VM

Firewall: UFW (Uncomplicated Firewall)

Network Scanning: Nmap

Other Tools: Terminal/Command Line

4. Steps Involved
   Install and Enable UFW
   Reset Existing Rules
   Set Default Policies
   Allow Only Required Services
   Block Ping
   Simulate Blocked Ping
   Simulate Blocked Port Scan

5. Results / Outputs

UFW Status: Only ports 22 (SSH) and 80 (HTTP) allowed.
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/c4ed6738-c808-41f7-b9c1-c921ed561e26" />


Blocked Ping: Request timed out confirms ICMP is blocked.
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/fd38ff7c-7a37-4032-a0fe-f275332b4b1c" />


Port Scan (Nmap): Only 22 and 80 open; other ports filtered.
<img width="824" height="609" alt="image" src="https://github.com/user-attachments/assets/9bd1dee3-fda0-4270-9838-7fe039fc67a3" />

Conclusion

The firewall successfully restricts access to only the required services (SSH and HTTP) while blocking all other traffic. Blocked ping and filtered ports demonstrate the effectiveness of the firewall. This project highlights the importance of firewall configuration in securing networked systems.


