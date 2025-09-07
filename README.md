# 🔎 Broken Link Hijacking Scanner

A Python tool to find **broken social media links** on websites that could lead to **subdomain takeover / account hijacking** opportunities.

## 🚀 Features
- Scans domains & subdomains (uses [subfinder](https://github.com/projectdiscovery/subfinder) if installed).
- Extracts all links from web pages.
- Detects broken/unclaimed **social media links** (Instagram, Twitter, GitHub, LinkedIn, etc.).
- Multi-threaded scanning for faster results.
- Logs all output and saves vulnerable links to a file.

---

## ⚠️ Important Note

- In **India**, TikTok is banned.  
- Because of this, **all TikTok links may appear as broken / vulnerable** when scanned.  
- Please **verify TikTok results manually** before reporting them as vulnerable.
    
---

📦 Installation

1. Clone the repository:
```bash
   git clone https://github.com/sayoojpkey/broken-link-scanner.git
   cd broken-link-scanner

2. Install required dependencies:
   pip install -r requirements.txt


3. 🛠️ Usage

   Prepare a file domains.txt with one domain per line:

   example.com
   testsite.org
   blaa.com

4. Run the scanner:

   python3 scanner.py -l domains.txt -o results.txt -t 10

   -l → File containing list of domains

   -o → Output file (default: output.txt)

   -t → Number of threads (default: 5)
