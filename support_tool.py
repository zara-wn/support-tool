import requests
import socket
import subprocess
import time
import platform
import os
from datetime import datetime

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Create a timestamped log file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_path = f"logs/log_{timestamp}.txt"

def write_log(message):
    print(message)
    with open(log_file_path, "a") as f:
        f.write(message + "\n")

def http_check(url):
    write_log(f"\n== HTTP check: {url} ==")
    try:
        start = time.time()
        r = requests.get(url, allow_redirects=True, timeout=5)
        elapsed = time.time() - start
        write_log(f"Status code: {r.status_code}")
        write_log(f"Final URL: {r.url}")
        write_log(f"Elapsed time: {elapsed:.2f}s\n")
        write_log("Response headers:")
        for k, v in r.headers.items():
            write_log(f"  {k}: {v}")
        cache_hdrs = {h: r.headers[h] for h in r.headers if 'cache' in h.lower() or h.lower() in ('age','etag','expires')}
        if cache_hdrs:
            write_log("\nCache-related headers (quick view):")
            for k,v in cache_hdrs.items():
                write_log(f"  {k}: {v}")
    except requests.exceptions.RequestException as e:
        write_log(f"Error fetching URL: {e}")

def dns_lookup(url):
    try:
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
        ip_address = socket.gethostbyname(hostname)
        write_log(f"\n== DNS Lookup: {hostname} ==")
        write_log(f"Hostname: {hostname}")
        write_log(f"IP Address: {ip_address}")
        return hostname
    except Exception as e:
        write_log(f"\nDNS Lookup failed: {e}")
        return None

def ping_host(hostname):
    write_log(f"\n== Ping: {hostname} ==")
    param = "-n" if platform.system().lower()=="windows" else "-c"
    cmd = ["ping", param, "4", hostname]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        write_log("Ping failed. Host may be unreachable.")

def traceroute_host(hostname):
    write_log(f"\n== Traceroute: {hostname} ==")
    cmd_name = "tracert" if platform.system().lower()=="windows" else "traceroute"
    cmd = [cmd_name, hostname]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        write_log("Traceroute failed. Host may be unreachable.")

def main():
    write_log("Support Troubleshooting Toolkit - HTTP, DNS, Ping & Traceroute Checker")
    url = input("Enter URL to check (e.g. https://example.com): ").strip()
    if not url:
        write_log("No URL provided. Exiting.")
        return
    http_check(url)
    hostname = dns_lookup(url)
    if hostname:
        ping_host(hostname)
        traceroute_host(hostname)
    write_log(f"\nLog saved to {log_file_path}")

if __name__ == "__main__":
    main()
