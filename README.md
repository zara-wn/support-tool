# Support Troubleshooting Toolkit

A lightweight Python tool to perform quick web and network diagnostics — designed for support engineers or anyone needing to check if a site is reachable and view its DNS and HTTP details.

---

## 🧩 Features

- ✅ HTTP status code & redirect tracking  
- 🌐 DNS lookup (IP resolution)  
- 🧠 Simple, interactive CLI  
- ⚙️ Lightweight — built with only the `requests` and `socket` libraries  

---

## ⚙️ How to Build This Project from Scratch

### 1. Create Your Project Folder
```bash
mkdir support-tool
cd support-tool

2. Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install requests

4. Create the Main Python File
nano support_tool.py


Then paste this code inside it:

import requests
import socket
import time

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
        print(f"IP Addresses: {ip_address}")
    except Exception as e:
        print(f"\nDNS Lookup failed: {e}")

def main():
    print("Support Troubleshooting Toolkit - HTTP & DNS Checker")
    url = input("Enter URL to check (e.g. https://example.com): ").strip()
    if not url:
        print("No URL provided. Exiting.")
        return
    http_check(url)
    dns_lookup(url)

if __name__ == "__main__":
    main()


Save with Ctrl + O, press Enter, then Ctrl + X.

▶️ How to Run the Tool

Run your project inside the virtual environment:

python3 support_tool.py


Enter any URL (for example):

https://google.com


You’ll see both an HTTP response and DNS lookup results.

🧪 Example Output
== HTTP check: https://google.com ==
Status code: 200
Final URL: https://www.google.com/
Elapsed time: 0.29s

== DNS Lookup: google.com ==
Hostname: google.com
IP Addresses: 172.217.12.142

🧰 Common Fixes

If you get an error like command not found:

Make sure you’re in the same folder as support_tool.py

Run the tool with python3 support_tool.py

Ensure requests is installed with pip install requests

🚀 Next Steps / Enhancements

Add ping or traceroute features

Export logs to JSON or text file

Add CLI arguments (argparse) for automation

🪪 License

MIT License


---

### ✅ STEP 3: Save & Exit Nano
- Press **Ctrl + O**, then **Enter** to save  
- Press **Ctrl + X** to exit  

---

### ✅ STEP 4: Confirm the README Exists
Type:
```bash
ls


You should now see:

support_tool.py  support_tool.py.bak  support-tool.py  venv  README.md

✅ STEP 5: Create a .gitignore File (to exclude venv)

Run:

nano .gitignore


Paste this:

venv/
__pycache__/
*.pyc


Save with Ctrl + O, Enter, then Ctrl + X.





✅ STEP 6: Initialize Git & Push to GitHub

Initialize a git repo:

git init


Add all files:

git add .


Commit your work:

git commit -m "Initial commit - Support Troubleshooting Toolkit"


Go to GitHub
 → create a new repository named:

support-tool


Then, back in your terminal, connect it:

git remote add origin https://github.com/YOUR_USERNAME/support-tool.git


Push it:

git branch -M main
git push -u origin main
