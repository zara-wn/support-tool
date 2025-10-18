# 002 - TLS handshake failure for www.example-app.com

**Summary:**  
Users report TLS handshake errors when accessing `https://www.example-app.com` from some regions.

**Steps to reproduce:**  
1. `python3 support_tool.py` -> run HTTP check against `https://www.example-app.com` -> error: SSL handshake failed.  
2. `openssl s_client -connect www.example-app.com:443 -servername www.example-app.com` -> shows certificate chain and expiry date.  
3. `dig +short www.example-app.com` -> IP addresses returned correctly.

**Findings:**  
- OpenSSL output shows leaf certificate expired on `2025-09-29`.  
- Some CDN edge POPs still served expired certificate due to cache/rollout issues.  
- Origin served renewed cert correctly.

**Action taken:**  
- Purged edge caches for TLS config.  
- Coordinated with Deployment team to re-deploy certificate across POPs and validate chain.  
- Suggested monitoring alert for cert expiry (30/14/7/3/1-day warnings).

**Resolution:**  
Rollout completed; TLS handshake successful globally. Suggested adding an automated cert expiry monitor.

**Attachments:**  
- `openssl s_client` output  
- certificate `notAfter` screenshot
