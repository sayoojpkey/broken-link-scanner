#!/usr/bin/env python3
import requests
import subprocess
import argparse
from bs4 import BeautifulSoup
import logging
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init

# Initialize colored output
init(autoreset=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("scan.log"), logging.StreamHandler()]
)

SOCIAL_DOMAINS = [
    "instagram.com", "twitter.com", "facebook.com",
    "github.com", "linkedin.com", "youtube.com",
    "tiktok.com", "medium.com"
]

def get_subdomains(domain):
    """Find subdomains using subfinder (if installed)."""
    try:
        result = subprocess.check_output(["subfinder", "-silent", "-d", domain])
        return result.decode().splitlines()
    except FileNotFoundError:
        logging.warning("subfinder not found, continuing without subdomain scan.")
        return []
    except Exception as e:
        logging.error(f"Subdomain scan failed for {domain}: {e}")
        return []

def is_valid_url(url):
    """Check if the URL is well-formed."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def extract_links(url, session):
    """Extract all links from a webpage."""
    links = []
    try:
        res = session.get(url, timeout=10)
        if res.status_code != 200:
            return []
        soup = BeautifulSoup(res.text, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("/") and is_valid_url(url):
                # Convert relative → absolute
                href = url.rstrip("/") + href
            if is_valid_url(href):
                links.append(href)
    except Exception as e:
        logging.warning(f"Failed to extract links from {url}: {e}")
    return links

def check_social(link, session):
    """Check if a social media link is broken/unclaimed."""
    try:
        r = session.get(link, timeout=10, allow_redirects=True)
        if r.status_code == 404:
            return True
        if "not found" in r.text.lower() or "page isn’t available" in r.text.lower():
            return True
    except Exception as e:
        logging.warning(f"Failed to check {link}: {e}")
        return True  # suspicious if we cannot verify
    return False

def scan_domain(domain, session, output_file):
    """Scan a single domain for broken social media links."""
    logging.info(f"Scanning {domain}")
    subdomains = get_subdomains(domain) + [domain]
    results = []

    for sub in subdomains:
        url = f"http://{sub}" if not sub.startswith(("http://", "https://")) else sub
        links = extract_links(url, session)
        for link in links:
            if any(social in link for social in SOCIAL_DOMAINS):
                if check_social(link, session):
                    result = f"[POSSIBLE HIJACK] {link} (found on {url})"
                    results.append(result)
                    print(Fore.RED + result + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + f"[SAFE] {link}" + Style.RESET_ALL)

    # Save only vulnerable results
    with open(output_file, "a") as f:
        for result in results:
            f.write(result + "\n")

def main():
    parser = argparse.ArgumentParser(description="Broken Link Hijacking Scanner")
    parser.add_argument("-l", "--list", help="File containing list of domains", required=True)
    parser.add_argument("-o", "--output", help="Output file for results", default="output.txt")
    parser.add_argument("-t", "--threads", help="Number of threads to use", type=int, default=5)
    args = parser.parse_args()

    with open(args.list, "r") as f:
        domains = [line.strip() for line in f if line.strip()]

    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(scan_domain, domain, session, args.output) for domain in domains]
        for future in as_completed(futures):
            future.result()

    logging.info(f"Scan completed. Vulnerabilities saved to {args.output}")

if __name__ == "__main__":
    main()
