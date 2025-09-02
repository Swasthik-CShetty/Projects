#!/usr/bin/env python3
from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

# Callback function to process each packet
def packet_callback(packet):
    log = f"{datetime.now()} | "

    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        log += f"IP {src} -> {dst} | Proto: {proto}"

        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            log += f" | TCP {sport} -> {dport}"

        elif packet.haslayer(UDP):
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            log += f" | UDP {sport} -> {dport}"

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            log += f" | Payload: {payload[:30]}..."  # first 30 bytes

        print(log)

        # Save to file
        with open("packet_logs.txt", "a") as f:
            f.write(log + "\n")

# Start sniffing (filtering only TCP packets here, you can change)
print("[*] Starting packet sniffer... Press Ctrl+C to stop")
sniff(filter="tcp", prn=packet_callback, store=False)
