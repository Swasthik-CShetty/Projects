# Analysing Website Security Headers

## Overview
This project analyzes the **security headers** of various websites using online tools such as [SecurityHeaders.com](https://securityheaders.com/) and [WhyNoPadlock.com](https://www.whynopadlock.com/).  
The goal is to identify missing or misconfigured headers, check SSL/TLS configurations, and suggest improvements based on security best practices.

## Tools Used
- **SecurityHeaders.com** → To scan and grade websites based on implemented HTTP security headers.  
- **WhyNoPadlock.com** → To verify SSL/TLS certificates, HTTPS enforcement, and mixed content issues.

## Websites Analyzed & Results

| Website                | Grade | Missing Headers                                                                 | HTTPS Enforced | SSL Status & Expiry         |
|------------------------|-------|---------------------------------------------------------------------------------|----------------|-----------------------------|
| **YouTube.com**        | A     | Referrer-Policy                                                                 | Yes            | Valid (SHA256), expires in 45 days |
| **OWASP Juice Shop**   | D     | Strict-Transport-Security, Content-Security-Policy, Referrer-Policy, Permissions-Policy | No     | Valid (SHA256), expires 15 Oct 2025 |
| **Itsecgames.com**     | F     | Content-Security-Policy, X-Frame-Options, X-Content-Type-Options ,Referrer-Policy, Permissions-Policy| No  | Valid (SHA256), domain mismatch, expires in 81 days |
| **Ujartechsolutions.in**| A    | Referrer-Policy, Permissions-Policy                                             | Yes            | Valid (ECDSA), expires 20 Oct 2025 |

## Key Security Headers
- **Strict-Transport-Security (HSTS):** Forces secure HTTPS connections.  
- **Content-Security-Policy (CSP):** Prevents cross-site scripting (XSS) and data injection attacks.  
- **X-Frame-Options:** Protects against clickjacking attacks.  
- **X-Content-Type-Options:** Stops browsers from MIME-sniffing files.  
- **Referrer-Policy:** Controls how much referrer information is sent.  
- **Permissions-Policy:** Restricts use of browser features like camera, microphone, and location.

## Conclusion
- Websites with higher grades (A) have strong security headers but still lack certain modern privacy headers.  
- Lower-graded sites (D/F) are more vulnerable due to missing critical headers and lack of HTTPS enforcement.  
- **Recommendation:** Implement all relevant security headers and enforce HTTPS on all pages for maximum security.

