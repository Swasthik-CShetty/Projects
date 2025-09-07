Malware Static Analysis Report
1. Introduction

This report documents the static analysis of a suspicious executable named invoice_2318362983713_823931342io.pdf.exe. The objective is to assess whether the file is malicious, identify its potential capabilities, and provide supporting evidence from multiple analysis tools.

2. Abstract

The executable was analyzed with Linux tools (file, hexdump, strings), Windows pestudio, and VirusTotal. Results confirm it is a Windows Portable Executable (PE32), masquerading as a PDF. The file contains suspicious API imports, obfuscated code, persistence mechanisms, and network-related functions. VirusTotal results strongly confirm the malware classification with multiple vendor detections.

3. Tools Used

Linux Tools

file, hexdump, strings


Online Service

VirusTotal

Environment

Isolated Kali Linux 

4. Steps Involved in Analysis
Step 1: File Identification
Step 2: Hexdump

MZ header present → Windows executable.

PE\0\0 signature confirms valid PE file.

No %PDF magic bytes → fake PDF.

Step 3: Strings Analysis

Key findings:

VirtualAlloc, InternetOpenUrlA, GetAsyncKeyState → indicators of process injection, keylogging, and network communication.

Clipboard and registry function calls → persistence & credential theft.

Obfuscated strings suggest packing.


Step 4: VirusTotal Analysis

Hash: 69e966e730557fde8fd84317cdef1ece00a8bb3470c0b58f3231e170168af169

Detection: 63/72 vendors flagged as malicious.

Threat Labels:

Trojan.ZAccess / Sirefef

Backdoor.Win32.Obfuscator

Trojan.ZeroAccess.RN

Tags: persistence, self-delete, detect-debug-environment, suspicious-udp, via-tor etc

5. Outputs

file command output.

Hexdump showing MZ header.

strings output with API calls.

VirusTotal result (63/72 detection).

6. Conclusion

The file invoice_2318362983713_823931342io.pdf.exe is confirmed to be malware, specifically a Zeus/ZAccess trojan variant. Static analysis showed strong signs of malicious intent: suspicious API calls, fake PDF disguise, obfuscation, persistence mechanisms, and network capabilities. VirusTotal results reinforce the findings with 63/72 detections, including backdoor and trojan classifications.

This malware is designed for credential theft, persistence, and remote access, and should not be executed outside of a secure sandbox or VM environment.
