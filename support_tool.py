import requests
import socket
import subprocess
import time
import platform

def http_check(url):
    print(f"\n== HTTP check: {url} ==")
    try:
        start = time.time()
        r = requests.get(url, allow_redirects=True, timeout=5)
        elapsed = time.time() - start
        print(f"Status code: {r.status_code}")
        print(f"Final URL: {r.url}")
        print(f"Elapsed time: {elapsed:.2f}s\n")
        print("Response headers:")
        for k, v in r.headers.items():
            print(f"  {k}: {v}")

        cache_hdrs = {h: r.headers[h] for h in r.headers if 'cache' in h.lower() or h.lower() in ('age','etag','expires')}
        if cache_hdrs:
            print("\nCache-related headers (quick view):")
            for k,v in cache_hdrs.items():
                print(f"  {k}: {v}")
    except requests.exceptions.RequestException as e:
        print("Error fetching URL:", e)

def dns_lookup(url):
    try:
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
        ip_address = socket.gethostbyname(hostname)
        print(f"\n== DNS Lookup: {hostname} ==")
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
        return hostname
    except Exception as e:
        print(f"\nDNS Lookup failed: {e}")
        return None

def ping_host(hostname):
    print(f"\n== Ping: {hostname} ==")
    param = "-n" if platform.system().lower()=="windows" else "-c"
    cmd = ["ping", param, "4", hostname]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("Ping failed. Host may be unreachable.")

def traceroute_host(hostname):
    print(f"\n== Traceroute: {hostname} ==")
    cmd_name = "tracert" if platform.system().lower()=="windows" else "traceroute"
    cmd = [cmd_name, hostname]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("Traceroute failed. Host may be unreachable.")

def main():
    print("Support Troubleshooting Toolkit - HTTP, DNS, Ping & Traceroute Checker")
    url = input("Enter URL to check (e.g. https://example.com): ").strip()
    if not url:
        print("No URL provided. Exiting.")
        return
    http_check(url)
    hostname = dns_lookup(url)
    if hostname:
        ping_host(hostname)
        traceroute_host(hostname)

if __name__ == "__main__":
    main()
