Project 5: Web Directory Bruteforce
1. Introduction

The goal of this project is to discover hidden directories and endpoints on a test website. Many web applications have undiscovered paths that could expose sensitive information or allow unauthorized access. Using automated directory enumeration tools, we can identify such endpoints for analysis and mitigation.

2. Abstract

This project performs directory brute-forcing on a web application (Juice Shop) to detect hidden files, folders, and API endpoints. Discovering these paths helps understand potential security risks like exposed APIs, admin panels, and sensitive files. The project demonstrates how attackers might enumerate web content and highlights the importance of restricting access and implementing proper security measures.

3. Tools Used

Gobuster v3.8 – directory and file brute-forcing

Wordlists – /usr/share/wordlists/dirb/common.txt and Seclists directory-list-2.3-medium.txt

OS – Kali Linux 2025

Optional – Docker (to run local Juice Shop instance)

Command-line utilities – curl for verification

4. Steps Involved in Building the Project
    Prepare the Target

    Used juice shop as a target
    Run Gobuster
    Analyze Results

Analyze Response Codes
   
Path	Status	Size	Analysis
/api	500	2857	API endpoint exists but crashed → may reveal backend info.
/apis	500	2859	Same as /api, another API entry point.
/assets/	301	156	Redirect → static files folder, may reveal JS/CSS.
/ftp	200	12462	Accessible → could expose files or test uploads.
/profile	500	1036	Profile functionality → crashed, could leak info.
/promotion	200	6586	Public endpoint → may expose business logic.
/redirect	500	2959	Redirect feature → may be vulnerable to open redirects.
/rest	500	2859	REST API route → backend functionality exposed.
/restaurants	500	2873	Likely part of ordering → may contain data.
/restore	500	2865	Backup/restore feature → sensitive functionality.
/restricted	500	2871	Restricted/admin area → should be protected.
/restored	500	2867	Related to restore → sensitive.
/robots.txt	200	28	Can reveal hidden paths.
/video	200	10MB	Large media file → may be abused for DoS.
/Video	200	10MB	Same as above (case-sensitive)

Ways to Restrict Access

Path / Category	Restriction / Security Measure
API Endpoints (/api, /rest)	Require authentication & authorization; validate inputs; handle errors properly.
Admin / Restricted Areas (/restricted)	Restrict access via login, IP whitelist, or VPN.
Backup / Restore (/restore, /restored)	Move out of web root; only admins can access; log usage.
File Storage (/ftp)	Protect with auth; move outside web root; disable direct HTTP access.
Static Assets (/assets/)	Avoid sensitive info in JS/CSS; use access control if needed.
Robots.txt	Don’t list sensitive directories.
Redirects (/redirect)	Sanitize inputs to prevent open redirect attacks.
Large Media Files (/video)	Use streaming or access control; limit file size.
Internal Errors (500)	Serve generic error pages; log details internally.

Conclusion

This project demonstrates how directory brute-forcing can uncover hidden endpoints in a web application. By analyzing response codes, we identified public, restricted, and error-prone paths. The exercise emphasizes the importance of:

Securing API endpoints and admin areas

Protecting sensitive files

Implementing proper error handling and input validation

Through this project, the methodology of web enumeration and the risks associated with exposed directories were understood, along with practical ways to mitigate them.



