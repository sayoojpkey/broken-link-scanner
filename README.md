# 🔎 Broken Link Hijacking Scanner

A Python tool to find **broken social media links** on websites that could lead to **subdomain takeover / account hijacking** opportunities.

## 🚀 Features
- Scans domains & subdomains (uses [subfinder](https://github.com/projectdiscovery/subfinder) if installed).
- Extracts all links from web pages.
- Detects broken/unclaimed **social media links** (Instagram, Twitter, GitHub, LinkedIn, etc.).
- Multi-threaded scanning for faster results.
- Logs all output and saves vulnerable links to a file.

---

## 📦 Installatione 

git clon https://github.com/sayoojpkey/broken-link-scanner 

Prepare a domain list (e.g., domains.txt):

example.com
testsite.org


## Run the scanner:

python3 scanner.py -l domains.txt -o results.txt -t 10


-l → File containing domains

-o → Output file (default: output.txt)

-t → Number of threads (default: 5)

## Check the results

Vulnerable links → saved in results.txt

Logs → stored in scan.log
