# 🔎 Broken Link Hijacking Scanner

A Python tool to find **broken social media links** on websites that could lead to **subdomain takeover / account hijacking** opportunities.

## 🚀 Features
- Scans domains & subdomains (uses [subfinder](https://github.com/projectdiscovery/subfinder) if installed).
- Extracts all links from web pages.
- Detects broken/unclaimed **social media links** (Instagram, Twitter, GitHub, LinkedIn, etc.).
- Multi-threaded scanning for faster results.
- Logs all output and saves vulnerable links to a file.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/broken-link-scanner.git
   cd broken-link-scanner
