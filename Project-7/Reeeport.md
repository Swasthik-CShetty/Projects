Project 7: SSH Server Hardening
Objective

The objective of this project is to secure an SSH server against brute-force attacks and unauthorized access. SSH is the primary remote administration protocol for Linux servers, and hardening it ensures that only authorized users can connect, reducing the risk of compromise.

Abstract

This project demonstrates how to harden an SSH server by implementing multiple layers of security. It covers disabling root login, changing the default SSH port, restricting users, enabling public key authentication, and protecting against brute-force attacks using Fail2ban. The effectiveness of these configurations is verified by simulating unauthorized login attempts and observing the system’s response.

Tools Used

OpenSSH – to configure and manage SSH service.

Fail2ban – to monitor authentication failures and ban IPs attempting brute-force attacks.

iptables – for basic firewall rules (optional for added security).



Steps Involved in Building the Project

Step 1: Configure SSH to Disable Root Login
Step 2: Change Default Port and Restrict Users
Step 3: Set Up Public Key Authentication
Step 4: Install and Configure Fail2ban
Step 5: Test Brute-Force Protection

Screenshots / Sample Output

Successful SSH login with key:
swasthikcshetty@kali:~$ ssh -p 2222 swasthikcshetty@192.168.249.128
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.15.0-72-generic x86_64)

Failed login attempt:
ssh -p 2222 wronguser@192.168.249.128
wronguser@192.168.249.128: Permission denied (publickey)

Fail2ban banning after 3 failed attempts:
sudo fail2ban-client status sshd
Currently banned: 1
Banned IP list: 192.168.249.10


Conclusion

This project successfully hardened an SSH server by implementing multiple layers of security. Root login was disabled, the default port changed, and access restricted to authorized users. Public key authentication ensured secure logins without passwords. Fail2ban effectively blocked brute-force attacks, demonstrated by banning an IP after repeated failed attempts. Additional firewall rules with iptables provide another layer of defense. Overall, these configurations significantly improve the server’s security posture and protect against common SSH attacks.
