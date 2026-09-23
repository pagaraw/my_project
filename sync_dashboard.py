import os
import re
from datetime import datetime

print("=========================================")
print("🔄 EXECUTING ADVANCED DASHBOARD SYNC PIPELINE")
print("=========================================\n")

REPORT_FILE = "scan_report.txt"
METADATA_FILE = "network_metadata.txt"
DASHBOARD_FILE = "dashboard.html"

target_ip = "127.0.0.1"
open_ports = "0"
public_location = "Joliet, Illinois"
isp_provider = "Auto-Detecting"

# 1. Parse port scan metrics
if os.path.exists(REPORT_FILE):
    with open(REPORT_FILE, "r") as f:
        content = f.read()
        vuln_match = re.search(r"Open Service Risks Found:\s*(\d+)", content)
        if vuln_match: open_ports = vuln_match.group(1)

# 2. Parse live network metadata out of your text log
if os.path.exists(METADATA_FILE):
    print(f"Scraping active metadata out of {METADATA_FILE}...")
    with open(METADATA_FILE, "r") as f:
        content = f.read()
        ip_match = re.search(r"Public IP Address:\s*([\d\.]+)", content)
        loc_match = re.search(r"Node Location\s*:\s*(.*)", content)
        isp_match = re.search(r"Network Provider\s*:\s*(.*)", content)

        if ip_match: target_ip = ip_match.group(1)
        if loc_match: public_location = loc_match.group(1).strip()
        if isp_match: isp_provider = isp_match.group(1).strip()

# 3. Calculate dynamic workspace tracking sizing parameters
total_bytes = 0
for file in os.listdir("."):
    if file.endswith(".txt") or file.endswith(".sh") or file.endswith(".py") or file.endswith(".html"):
        total_bytes += os.path.getsize(file)

# 4. Inject all properties directly into your dashboard layout
if os.path.exists(DASHBOARD_FILE):
    with open(DASHBOARD_FILE, "r") as f:
        html = f.read()

    html = re.sub(r"Target Range Checked:.*</strong>", f"Target Range Checked:</strong> <strong style='color: #6366f1;'>{target_ip}</strong>", html)
    html = re.sub(r"Open Network Vulnerabilities:.*</strong>", f"Open Network Vulnerabilities:</strong> <strong style='color: #10b981;'>{open_ports} Exposed Ports</strong>", html)
    html = re.sub(r"Total Directory Footprint:.*</span>", f"Total Directory Footprint:</span> <span class='metric-value'>{total_bytes} Bytes</span>", html)
    html = re.sub(r"Host Node Profile:.*</p>", f"Host Node Profile: DELL-LAPTOP | Location: {public_location} | ISP: {isp_provider}</p>", html)

    with open(DASHBOARD_FILE, "w") as f:
        f.write(html)
    print("📊 Success: HTML Monitoring Dashboard updated with live network and file metrics!")
