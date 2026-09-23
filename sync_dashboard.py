import os
import re
from datetime import datetime

print("=========================================")
print("🔄 RUNNING VISUAL DASHBOARD DATA SYNC PIPELINE")
print("=========================================\n")

# Target asset tracking paths
REPORT_FILE = "scan_report.txt"
DASHBOARD_FILE = "dashboard.html"

# Default fallback statistics profile parameters
open_ports = "0"
target_ip = "127.0.0.1"

# 1. Parse your latest Network Port Scan data out of the text log
if os.path.exists(REPORT_FILE):
    print(f"Reading active metrics block inside {REPORT_FILE}...")
    with open(REPORT_FILE, "r") as f:
        content = f.read()
        # Use regex filters to extract telemetry variables out of plain log lines
        ip_match = re.search(r"Target Host Evaluated\s*:\s*([\d\.]+)", content)
        vuln_match = re.search(r"Total Vulnerabilities Located\s*:\s*(\d+)", content)
        
        if ip_match: target_ip = ip_match.group(1)
        if vuln_match: open_ports = vuln_match.group(1)
else:
    print(f"⚠️ Warning: {REPORT_FILE} not found. Utilizing default local profiles.")

# 2. Automatically measure your actual repository folder payload size in bytes
total_bytes = 0
for file in os.listdir("."):
    if file.endswith(".txt") or file.endswith(".sh") or file.endswith(".py") or file.endswith(".html"):
        total_bytes += os.path.getsize(file)

print(f"Calculated active source file inventory envelope size: {total_bytes} Bytes")

# 3. Read the dashboard HTML structure, inject the live variables, and rewrite it
if os.path.exists(DASHBOARD_FILE):
    with open(DASHBOARD_FILE, "r") as f:
        html = f.read()
    
    # Programmatically slice and swap text markers inside the html layout template
    html = re.sub(r"Target Evaluated:.*</strong>", f"Target Evaluated:</strong> <strong>{target_ip}</strong>", html)
    html = re.sub(r"Total Open Vulnerabilities:.*</strong>", f"Total Open Vulnerabilities:</strong> <strong>{open_ports}</strong>", html)
    html = re.sub(r"Total Storage Footprint:.*</strong>", f"Total Storage Footprint:</strong> <strong>{total_bytes} Bytes</strong>", html)
    html = re.sub(r"Host Profile Location:.*</p>", f"Host Profile Location: DELL-LAPTOP | Last Script Sync: {datetime.now().strftime('%M:%S')}</p>", html)
    
    with open(DASHBOARD_FILE, "w") as f:
        f.write(html)
    print(f"📊 Success: {DASHBOARD_FILE} has been programmatically updated with live system metrics!")
else:
    print(f"❌ Error: {DASHBOARD_FILE} structural template missing.")

print("\n=========================================")
