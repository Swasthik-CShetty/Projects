# BASIC NETWORK SCAN USING NMAP

**Author:** Swasthik C Shetty  
**Date:** 12 August 2025  

## 📌 Overview
Nmap (Network Mapper) is an open-source tool used to scan IP addresses, ports, and services in a network. It helps identify active hosts, running services, operating systems, and potential vulnerabilities.

---

## Commands Used

### 1. Scan a Single Host
Scans a single host for the **top 1000 well-known ports** (e.g., SQL, SNTP, Apache).
nmap scanme.nmap.org
### 2. Stealth Scan
Performs a TCP SYN scan by sending SYN packets and analyzing responses.
If a SYN/ACK is received → port is open.
nmap -sS scanme.nmap.org
### 3. Version Detection
Identifies versions of running applications/services.
Helps match services to known vulnerabilities (CVE database).
nmap -sV scanme.nmap.org
### 4. OS Detection
Attempts to identify the target's operating system.
nmap -O scanme.nmap.org
### 5. Aggressive Scan
Performs OS detection, version detection, script scanning, and traceroute in one command.
Provides more information but is easier to detect during security audits.
nmap -A scanme.nmap.org
### 6. All Ports Scan
Scans all 65,535 TCP ports instead of the default top 1000.
Takes longer but ensures no open port is missed.
nmap -p- scanme.nmap.org
### 7. Nmap Help
Displays all available flags and options.
nmap -h

## Observation
## SConclusion
