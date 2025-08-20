# Task 08 – Password Cracking with John the Ripper

##  Objective
To learn how hashed passwords can be cracked using **John the Ripper (JTR)**, understand password hashing, and the importance of strong password security.

---

##  Tools Used
- John the Ripper
- Kali Linux / Parrot OS
- Wordlist (custom + rockyou.txt)

---

## Steps Performed
1. Created a sample hash:
   echo -n 'mypassword' | openssl passwd -1 -stdin

2.Saved the hash in hash.txt
3.Cracked the password using john

## Learned
How password hashing works (MD5Crypt in this case).
How attackers use tools like John the Ripper to exploit weak passwords.
Importance of strong, complex, and salted passwords to defend against dictionary/brute-force attacks.

Hands-on experience in cracking a sample hash.
