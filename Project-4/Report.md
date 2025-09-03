Project Report: File Integrity Checker
1. Introduction

The purpose of this project is to detect file tampering using cryptographic hashing techniques. Files often serve as critical components in any operating system or application. Unauthorized modification of these files can compromise security. By storing and comparing file hashes, this project helps ensure file integrity and alerts the user if any changes are detected.

2. Abstract

The File Integrity Checker is a Python-based tool that uses SHA-256 (or MD5) hashing to detect file modifications. The project stores original file hashes in a secure JSON file and regularly verifies them. If a mismatch is detected, the tool alerts the user and records the incident in a log file. This project is useful for system administrators, developers, and cybersecurity practitioners who need to monitor files for tampering.

3. Tools Used

Operating System: Kali Linux

Programming Language: Python 3

Libraries:

hashlib → for generating file hashes (SHA-256/MD5)

json → for storing and retrieving file hashes

datetime → for timestamping logs

Utilities:

cron → for scheduling automated integrity checks

chmod / chattr → for securing hash and log files

4. Steps Involved in Building the Project

Setup project directory

Write the Python script (checker.py)

Store file hashes.

Check files against stored hashes.

Log activities with timestamps.

Generate baseline hashes

Verify integrity of files

Simulate tampering

View logs

Output :
<img width="1280" height="800" alt="Screenshot_2025-09-03_10_45_23" src="https://github.com/user-attachments/assets/85ce9ff1-73da-4e5a-94dd-86f63e3a993d" />

5. Conclusion

This project successfully demonstrates how file integrity can be monitored using hashing. The tool provides a simple yet effective way to detect unauthorized changes in files. By automating checks with cron, it ensures continuous monitoring. Through this project, I learned how to use hashing for security, work with JSON for structured data storage, and automate tasks using cron jobs.

6. Challenges Faced 

Encountered a JSONDecodeError when hashes.json was empty. Fixed it by re-initializing the file.

Needed to use absolute paths in cron jobs because relative paths caused failures.

Learned how to secure log files with Linux permissions to prevent tampering.

7. References

Python official documentation – hashlib

