# 🧰 Support Troubleshooting Toolkit

A lightweight Python tool to perform quick web and network diagnostics — designed for support engineers or anyone needing to check if a site is reachable and view its DNS and HTTP details.

---

## 🌟 Features

- ✅ HTTP status code & redirect tracking  
- 🌐 DNS lookup (IP resolution)  
- 🧠 Simple, interactive CLI  
- ⚙️ Lightweight — built only with `requests` and `socket`  
- 🧾 Includes real-world support case simulations (`tickets/`)

---

## ⚙️ How to Build This Project from Scratch

### 1️⃣ Create Your Project Folder
\`\`\`bash
mkdir support-tool
cd support-tool
\`\`\`

### 2️⃣ Set Up a Virtual Environment
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3️⃣ Install Dependencies
\`\`\`bash
pip install requests
\`\`\`

### 4️⃣ Create the Main Python File
\`\`\`bash
nano support_tool.py
\`\`\`

Paste this code inside it:

\`\`\`python
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

        cache_hdrs = {h: r.headers[h] for h in r.headers if 'cache' in h.lower() or h.lower() in ('age', 'etag', 'expires')}
        if cache_hdrs:
            print("\nCache-related headers (quick view):")
            for k, v in cache_hdrs.items():
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
\`\`\`

Save with **Ctrl + O**, **Enter**, then **Ctrl + X**.

---

## ▶️ How to Run the Tool

Run inside the virtual environment:

\`\`\`bash
python3 support_tool.py
\`\`\`

Example input:
https://google.com


Example output:


== HTTP check: https://google.com
 ==
Status code: 200
Final URL: https://www.google.com/

Elapsed time: 0.29s

== DNS Lookup: google.com ==
Hostname: google.com
IP Address: 172.217.12.142


---

## 🧾 Example Support Tickets

This folder simulates real troubleshooting tickets from a Customer Support Engineer’s workflow.

| Ticket | Summary | Example Issue |
|:-------|:---------|:--------------|
| `001-503-eu-edge.md` | Intermittent 503 errors for EU users | Regional connectivity issue |
| `002-tls-expired.md` | TLS handshake failure | Expired SSL certificate on app endpoint |

Each markdown file includes:
- Steps to reproduce  
- Findings  
- Actions taken  
- Resolution summary  
- Attachments or CLI command outputs  

Run this to list all tickets:
\`\`\`bash
ls tickets/
\`\`\`

---

## 🧰 Common Fixes

If you get:


command not found


✅ Make sure you’re in the same folder as `support_tool.py`  
✅ Run it with `python3 support_tool.py`  
✅ Install dependencies again with `pip install requests`

---

## 🚀 Future Enhancements

- Add `ping` or `traceroute` features  
- Export logs to `.json` or `.txt`  
- Add CLI arguments with `argparse`  
- Integrate AWS or API health checks  

---

## 🛠️ Support Toolkit Workflow

```text
User runs support_tool.py
          │
          ▼
     Input URL
          │
  ┌───────┼────────┐
  │       │        │
HTTP Check DNS Lookup Ping
          │
       Traceroute
          │
          ▼
   Outputs to terminal
(Optional: save to logs/)

---
📁 Project Structure

support-tool/
│
├─ README.md        <- Instructions, examples, tickets info
├─ LICENSE          <- MIT License
├─ requirements.txt <- Python dependencies
├─ support_tool.py  <- Main tool: HTTP, DNS, Ping, Traceroute
├─ tickets/         <- Sample troubleshooting cases
│   ├─ 001-503-eu-edge.md
│   └─ 002-tls-expired.md
├─ logs/            <- Stores output/logs if implemented later
└─ venv/            <- Python virtual environment


## 🪪 License

MIT License — see [LICENSE](LICENSE) for details.

---

### 🧑‍💻 Author
**Zara (zara-wn)**  
A cloud-focused engineer in training, building hands-on diagnostic tools and real-world support case simulations.
