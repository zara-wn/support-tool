#!/usr/bin/env python3
"""
Support Troubleshooting Toolkit
--------------------------------
A simple Python-based command-line tool for performing HTTP checks and DNS lookups.
Great for Cloud Support or Technical Support practice projects.
"""

import requests
import socket
import time

# HTTP Check Feature
def http_check(url):
    print(f"\n== HTTP check: {url} ==")
    try:
        start = time.time()
        r = requests.get(url, timeout=10)
        elapsed = time.time() - start

        print(f"Status code: {r.status_code}")
        print(f"Final URL: {r.url}")
        print(f"Elapsed time: {elapsed:.2f}s")

        print("\nResponse headers:")
        for k, v in r.headers.items():
            print(f"  {k}: {v}")

        # Quick cache-related view
        cache_hdrs = {
            h: r.headers[h]
            for h in r.headers
            if 'cache' in h.lower() or h.lower() in ('age', 'etag', 'expires')
        }
        if cache_hdrs:
            print("\nCache-related headers (quick view):")
            for k, v in cache_hdrs.items():
                print(f"  {k}: {v}")

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching URL:", e)

# DNS Lookup Feature
def dns_lookup(domain):
    print(f"\n== DNS Lookup: {domain} ==")
    try:
        hostname, aliases, ips = socket.gethostbyname_ex(domain)
        print("Hostname:", hostname)
        if aliases:
            print("Aliases:", ", ".join(aliases))
        print("IP Addresses:", ", ".join(ips))
    except socket.gaierror:
        print("❌ Could not resolve domain. Please check the spelling or try again.")
    except Exception as e:
        print("DNS Lookup failed:", e)

# Main function
def main():
    print("Support Troubleshooting Toolkit - HTTP & DNS Checker")
    url = input("Enter URL to check (e.g. https://example.com): ").strip()

    if not url:
        print("No URL provided. Exiting.")
        return

    http_check(url)

    # Extract hostname and run DNS lookup
    hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
    dns_lookup(hostname)

if __name__ == "__main__":
    main()










