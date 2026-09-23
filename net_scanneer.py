import socket
import sys
import threading
from datetime import datetime

print("=========================================")
print("🌐 ENTER TARGET SUITE ADDRESS")
print("=========================================")
user_input = input("Enter IP Address or Domain to audit (Press Enter for local sandbox 127.0.0.1): ").strip()

TARGET_HOST = user_input if user_input else "127.0.0.1"

PORTS_TO_SCAN = {
    21: "FTP (File Transfer Protocol - Cleartext)",
    22: "SSH (Secure Shell Secure Channel Link)",
    23: "Telnet (Legacy Unencrypted Terminal Console)",
    80: "HTTP (Standard Cleartext Web Servers)",
    139: "NetBIOS (Windows File Sharing Access Service)",
    443: "HTTPS (Secure SSL Encrypted Web Servers)",
    3389: "RDP (Remote Desktop Protocol Protocol Gateway)"
}

scan_start_time = datetime.now()

print("\n=========================================")
print(f"🔒 RUNNING COMPREHENSIVE MULTI-THREADED SCAN")
print(f"Target Infrastructure Matrix : {TARGET_HOST}")
print(f"Scan Initialized On Timeline: {scan_start_time}")
print("=========================================\n")

print_lock = threading.Lock()
open_ports_found = 0
report_lines = []

def audit_port(port, service_name):
    global open_ports_found
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    
    result = s.connect_ex((TARGET_HOST, port))
    
    with print_lock:
        if result == 0:
            status_msg = f"⚠️  ALERT: Port {port} is OPEN | Vector: {service_name}"
            open_ports_found += 1
        else:
            status_msg = f"🔒 Secure: Port {port} is closed/filtered."
        
        print(status_msg)
        report_lines.append(status_msg)
        
    s.close()

threads = []
for port_num, service_desc in PORTS_TO_SCAN.items():
    t = threading.Thread(target=audit_port, args=(port_num, service_desc))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# --- NEW AUTOMATED DIAGNOSTIC LOGGING ENGINE ---
REPORT_FILE = "scan_report.txt"
with open(REPORT_FILE, "w") as f:
    f.write("=========================================\n")
    f.write("📋 SECURITY NETWORK AUDIT DIAGNOSTIC REPORT\n")
    f.write("=========================================\n")
    f.write(f"Target Host Evaluated : {TARGET_HOST}\n")
    f.write(f"Scan Date Timestamp   : {scan_start_time}\n")
    f.write(f"Total Critical Vectors Checked: {len(PORTS_TO_SCAN)}\n")
    f.write(f"Total Vulnerabilities Located : {open_ports_found}\n")
    f.write("-----------------------------------------\n\n")
    f.write("Detailed Findings Matrix:\n")
    for line in sorted(report_lines):
        f.write(f"{line}\n")
    f.write("\n=========================================\n")

print("\n=========================================")
print("📈 SYSTEM SECURITY INVENTORY AUDIT COMPLETE")
print("=========================================")
print(f"Total Potentially Exposed Open Ports   : {open_ports_found}")
print(f"Structured Audit Logs Exported to      : {REPORT_FILE}")
print("=========================================\n")
