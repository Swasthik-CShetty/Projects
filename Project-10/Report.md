
# 🔐 Project Report: Password Cracking Challenge using John the Ripper

## 1. Introduction
The main goal of this project is to demonstrate how weak passwords can be cracked using John the Ripper, a popular password-cracking tool. By creating hashed passwords, applying different wordlists and rules, and analyzing the results, we highlight the importance of using strong password policies to ensure better security.

## 2. Abstract
Passwords are still one of the most widely used methods of authentication, but weak or common passwords make systems vulnerable to attacks. This project simulates a password-cracking scenario where hashed passwords (MD5/SHA1) are created and tested against various wordlists using John the Ripper. The project emphasizes how quickly weak passwords can be cracked and provides recommendations for stronger password practices.

## 3. Tools Used
- **Operating System:** Kali Linux 2024.2  
- **Password Cracking Tool:** John the Ripper  
- **Wordlists:** Custom `wordlist_demo.txt`, `rockyou.txt`  
- **Hash Algorithms:** MD5 and SHA1  
- **Editor:** Nano/Vim for creating hash files  

## 4. Steps Involved in Building the Project
1. **Step 1:** Create a list of plaintext passwords.  
2. **Step 2:** Generate hashes (MD5/SHA1) using shell commands.  
3. **Step 3:** Run John with a custom wordlist.  
4. **Step 4:** Use `rockyou.txt` for more coverage.  
5. **Step 5:** Display cracked results.  

## 5. Screenshots / Outputs
<img width="1280" height="800" alt="OutputScreenshot" src="https://github.com/user-attachments/assets/c88d0f2c-d100-45f5-bd54-85cbf2515cbd" />

<img width="1280" height="800" alt="OutputScreenshot" src="https://github.com/user-attachments/assets/38a208bf-d9d9-453f-9071-1655b4984644" />
<img width="1280" height="800" alt="Screenshot" src="https://github.com/user-attachments/assets/aa1ec083-5b49-4480-8405-35e9b4c832d8" />


### Sample Results Table
| Hash Type | Hash Value                           | Plaintext   | Status       |
|-----------|--------------------------------------|-------------|--------------|
| MD5       | 482c811da5d5b4bc6d497ffa98491e38     | password123 | ✅ Cracked   |
| MD5       | 8d4db54daf7d67db5f3c96e43f61c609     | admin2024   | ✅ Cracked   |
| MD5       | 0d107d09f5bbe40cade3de5c71e9e9b7     | letmein     | ✅ Cracked   |
| MD5       | 40be4e59b9a2a2b5dffb918c0e86b3d7     | welcome     | ✅ Cracked   |
| MD5       | d8578edf8458ce06fbc5bb76a58c5ca4     | qwerty      | ✅ Cracked   |
| MD5       | f25a2fc72690b780b2a14e140ef6a9e0     | iloveyou    | ✅ Cracked   |
| MD5       | 0571749e2ac330a7455809c6b0e7af90     | sunshine    | ✅ Cracked   |
| MD5       | b696aef7776367787253dc2acdd10279     | dragon99    | ✅ Cracked   |
| MD5       | 011e1338c48168b8c8841f2af1e8e82f     | Secret@123  | ❌ Not cracked |
| MD5       | 3cc31cd246149aec68079241e71e98f6     | Secur3!Pass | ❌ Not cracked |

## 6. Conclusion
This project demonstrated that weak or common passwords can be cracked within seconds using John the Ripper and publicly available wordlists. Out of 10 chosen passwords, 8 were successfully cracked, highlighting the danger of reusing predictable or dictionary-based passwords. Strong password policies and additional security measures are essential to defend against brute-force and dictionary attacks.

## 7. Challenges Faced
- Initially, `rockyou.txt` wordlist was missing and had to be installed/unzipped.  
- Some stronger passwords (`Secret@123`, `Secur3!Pass`) were not in the default wordlists.  
- Cracking times varied based on CPU performance and hash type.  

## 8. References
- [John the Ripper Official Documentation](https://www.openwall.com/john/)  
- Kali Linux Wordlists: `/usr/share/wordlists/`  
- [RockYou wordlist GitHub mirror](https://github.com/brannondorsey/naive-hashcat/releases/tag/data)
