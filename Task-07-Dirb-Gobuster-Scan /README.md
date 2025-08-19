# Task 07 – Directory & File Enumeration (Dirb)

## Target
- **Target Used:** http://testphp.vulnweb.com (legal test server for practicing security testing)

## Tools Used
- **Dirb** (v2.22, pre-installed in Kali Linux)  
- Wordlist: `/usr/share/wordlists/dirb/common.txt`  


## Command Executed
dirb http://testphp.vulnweb.com /usr/share/wordlists/dirb/common.txt

## sample output
GENERATED WORDS: 4612

---- Scanning URL: http://testphp.vulnweb.com/ ----
==> DIRECTORY: http://testphp.vulnweb.com/admin/
+ http://testphp.vulnweb.com/cgi-bin (CODE:403|SIZE:276)
+ http://testphp.vulnweb.com/cgi-bin/ (CODE:403|SIZE:276)
+ http://testphp.vulnweb.com/crossdomain.xml (CODE:200|SIZE:224)
==> DIRECTORY: http://testphp.vulnweb.com/CVS/
+ http://testphp.vulnweb.com/CVS/Entries (CODE:200|SIZE:1)
+ http://testphp.vulnweb.com/CVS/Repository (CODE:200|SIZE:8)
+ http://testphp.vulnweb.com/CVS/Root (CODE:200|SIZE:1)
+ http://testphp.vulnweb.com/favicon.ico (CODE:200|SIZE:894)
==> DIRECTORY: http://testphp.vulnweb.com/images/
+ http://testphp.vulnweb.com/index.php (CODE:200|SIZE:4958)
==> DIRECTORY: http://testphp.vulnweb.com/pictures/
==> DIRECTORY: http://testphp.vulnweb.com/secured/
==> DIRECTORY: http://testphp.vulnweb.com/vendor/
## Findings
cgi-bin
crossdomainxml
cvs
fevicon.ico
images
pictures
secured
vendor

##Explanation of HTTP Status Codes
200 OK → Resource exists and is accessible
301/302 Redirect → Resource exists but redirects to another location
403 Forbidden → Resource exists but access is denied
500 Internal Server Error → Server error when requesting the resource
