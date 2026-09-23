import os
import re
import sqlite3
from datetime import datetime

print("=========================================")
print("🔄 EXECUTING RE-ENGINEERED DATABASE-DASHBOARD SYNC")
print("=========================================\n")

REPORT_FILE = "scan_report.txt"
METADATA_FILE = "network_metadata.txt"
DASHBOARD_FILE = "dashboard.html"
DB_FILE = "workspace_telemetry.db"

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

# 2. Parse live network metadata out of text log
if os.path.exists(METADATA_FILE):
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
    if file.endswith(".txt") or file.endswith(".sh") or file.endswith(".py") or file.endswith(".html") or file.endswith(".db"):
        total_bytes += os.path.getsize(file)

# 4. Pull history tracking logs out of your SQLite Database table rows
table_html = ""
if os.path.exists(DB_FILE):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, file_count, total_storage FROM system_logs ORDER BY id DESC LIMIT 5")
        rows = cursor.fetchall()

        table_html = """
        <div class="card" style="grid-column: 1 / -1; border-top-color: #6366f1; margin-top: 25px;">
            <h2>📋 SQLite Transaction History Log</h2>
            <table style="width: 100%; border-collapse: collapse; margin-top: 15px; text-align: left; font-size: 14px;">
                <thead>
                    <tr style="border-bottom: 2px solid #1f2937; color: #6366f1;">
                        <th style="padding: 10px;">Log ID</th>
                        <th style="padding: 10px;">Timestamp</th>
                        <th style="padding: 10px;">Tracked Files</th>
                        <th style="padding: 10px;">Storage Footprint</th>
                    </tr>
                </thead>
                <tbody>
        """
        for row in rows:
            table_html += f"""
                    <tr style="border-bottom: 1px solid #1f2937;">
                        <td style="padding: 10px; color: #9ca3af;">#{row[0]}</td>
                        <td style="padding: 10px;">{row[1]}</td>
                        <td style="padding: 10px;">{row[2]} Modules</td>
                        <td style="padding: 10px; color: #f59e0b; font-family: monospace;">{row[3]} Bytes</td>
                    </tr>
            """
        table_html += "</tbody></table></div>"
        conn.close()
    except Exception as e:
        table_html = f"<p style='color: red;'>Database Sync Error: {e}</p>"

# 5. Inject properties and database table directly into your dashboard layout file
if os.path.exists(DASHBOARD_FILE):
    with open(DASHBOARD_FILE, "r") as f:
        html = f.read()

    html = re.sub(r"Target Range Checked:.*</strong>", f"Target Range Checked:</strong> <strong style='color: #6366f1;'>{target_ip}</strong>", html)
    html = re.sub(r"Open Network Vulnerabilities:.*</strong>", f"Open Network Vulnerabilities:</strong> <strong style='color: #10b981;'>{open_ports} Exposed Ports</strong>", html)
    html = re.sub(r"Total Directory Footprint:.*</span>", f"Total Directory Footprint:</span> <span class='metric-value'>{total_bytes} Bytes</span>", html)
    html = re.sub(r"Host Node Profile:.*</p>", f"Host Node Profile: DELL-LAPTOP | Location: {public_location} | ISP: {isp_provider}</p>", html)

    # Inject or update the dynamic table container section inside the HTML layout grid
    if "<!-- TABLE_START -->" in html:
        html = re.sub(r"<!-- TABLE_START -->.*<!-- TABLE_END -->", f"<!-- TABLE_START -->{table_html}<!-- TABLE_END -->", html, flags=re.DOTALL)
    else:
        html = html.replace("</div>\n    </div>\n</body>", f"<!-- TABLE_START -->{table_html}<!-- TABLE_END -->\n        </div>\n    </div>\n</body>")

    with open(DASHBOARD_FILE, "w") as f:
        f.write(html)
    print("📊 Success: Web panel grid generated and populated with SQLite rows!")
