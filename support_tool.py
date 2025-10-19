import requests
import socket
import subprocess
import time
import platform
import os
from datetime import datetime
import argparse
import json

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Argument parser
parser = argparse.ArgumentParser(description="Support Troubleshooting Toolkit - HTTP, DNS, Ping & Traceroute Checker")
parser.add_argument('--url', type=str, help='URL to check (e.g. https://example.com)')
parser.add_argument('--nolog', action='store_true', help='Skip writing logs')
parser.add_argument('--json', action='store_true', help='Save logs in JSON format')
args = parser.parse_args()

# Timestamped log files
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_path_txt = f"logs/log_{timestamp}.txt"
log_file_path_json = f"logs/log_{timestamp}.json"

# Store JSON data
log_data = {
    "url": "",
    "http": {},
    "dns": {},
    "ping": [],
    "traceroute": []
}

def write_log(message):
    print(message)
    if not args.nolog and not args.json:
        with open(log_file_path_txt, "a") as f:
            f.write(message + "\n")

def http_check(url):
    write_log(f"\n== HTTP check: {url} ==")
    log_data["url"] = url
    try:
        start = time.time()
        r = requests.get(url, allow_redirects=True, timeout=5)
        elapsed = time.time() - start
        http_info = {
            "status_code": r.status_code,
            "final_url": r.url,
            "elapsed_time": elapsed,
            "headers": dict(r.headers)
        }
        log_data["http"] = http_info
        write_log(f"Status code: {r.status_code}")
        write_log(f"Final URL: {r.url}")
        write_log(f"Elapsed time: {elapsed:.2f}s\n")
        write_log("Response headers:")
        for k, v in r.headers.items():
            write_log(f"  {k}: {v}")
    except requests.exceptions.RequestException as e:
        write_log(f"Error fetching URL: {e}")

def dns_lookup(url):
    try:
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
        ip_address = socket.gethostbyname(hostname)
        dns_info = {"hostname": hostname, "ip": ip_address}
        log_data["dns"] = dns_info
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
        output = subprocess.check_output(cmd, universal_newlines=True)
        write_log(output)
        log_data["ping"].append(output)
    except subprocess.CalledProcessError:
        write_log("Ping failed. Host may be unreachable.")

def traceroute_host(hostname):
    write_log(f"\n== Traceroute: {hostname} ==")
    cmd_name = "tracert" if platform.system().lower()=="windows" else "traceroute"
    cmd = [cmd_name, hostname]
    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
        write_log(output)
        log_data["traceroute"].append(output)
    except subprocess.CalledProcessError:
        write_log("Traceroute failed. Host may be unreachable.")

def main():
    write_log("Support Troubleshooting Toolkit - HTTP, DNS, Ping & Traceroute Checker")
    url = args.url
    if not url:
        url = input("Enter URL to check (e.g. https://example.com): ").strip()
    if not url:
        write_log("No URL provided. Exiting.")
        return
    http_check(url)
    hostname = dns_lookup(url)
    if hostname:
        ping_host(hostname)
        traceroute_host(hostname)
    if not args.nolog:
        write_log(f"\nLog saved to {log_file_path_txt}")
    if args.json:
        with open(log_file_path_json, "w") as jf:
            json.dump(log_data, jf, indent=4)
        write_log(f"JSON log saved to {log_file_path_json}")

if __name__ == "__main__":
    main()
