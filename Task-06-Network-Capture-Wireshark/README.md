# Task 06 – Capturing Network Traffic Using Wireshark

##  Tools Used
- Wireshark 
---

## 📌 Steps Performed
1. Installed Wireshark and ran it with administrator/root permissions.  
2. Selected the active network interface.  
3. Started live capture.  
4. Generated traffic:
   - Visited `http://example.com` (HTTP – unencrypted).  
   - Pinned `google.com` (`ping google.com`) – ICMP traffic.  
5. Stopped capture.  
6. Applied filters to analyze protocols:
   - `http` – Inspect web requests & responses.  
   - `dns` – View domain name resolution queries.  
   - `tcp` – Observe 3-way handshake and data transfer.  
   - `udp` – Check for connectionless traffic.  
   - `icmp` – Verify ping packets.  
7. Saved capture as `capture.pcap`.

---

## 🔍 Filters Used
- **HTTP Requests** → `http.request`  
- **DNS Queries** → `dns`  
- **TCP 3-Way Handshake** → `tcp.flags.syn == 1 && tcp.flags.ack == 0`  
- **ICMP Traffic** → `icmp`  
- **UDP Traffic** → `udp`  

---

## 📊 Interesting Findings
1. **DNS Lookup**  
   - Observed query for `example.com` resolving to its IP address.  

2. **TCP Handshake**  
   - Verified the `SYN → SYN/ACK → ACK` sequence establishing a connection.  

3. **HTTP Traffic**  
   - In case of unencrypted HTTP, could see request headers like `User-Agent` and `Host`.  

4. **ICMP Packets**  
   - Clear request/reply when pinging `google.com`.  

5. **Encrypted vs Unencrypted**  
   - HTTP traffic showed visible payloads.  
   - HTTPS traffic was encrypted (only TLS handshake visible).  

---

## Security Observations
- **Unencrypted communication (HTTP)** can reveal sensitive info (clear-text data).  
- **DNS queries** show domains contacted by the system (can help in detecting suspicious/malware domains).  
- **TCP retransmissions** may indicate network issues or suspicious activity.  
- **ICMP** can be abused for reconnaissance (ping sweeps).  

---
