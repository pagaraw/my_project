import socket
import sys
import threading
from datetime import datetime

# --- OPTION 1: DYNAMIC TERMINAL USER INPUT ---
print("=========================================")
print("🌐 ENTER TARGET SUITE ADDRESS")
print("=========================================")
user_input = input("Enter IP Address or Domain to audit (Press Enter for local sandbox 127.0.0.1): ").strip()

TARGET_HOST = user_input if user_input else "127.0.0.1"

# A critical baseline index mapping common technical vector services
PORTS_TO_SCAN = {
    21: "FTP (File Transfer Protocol - Cleartext)",
    22: "SSH (Secure Shell Secure Channel Link)",
    23: "Telnet (Legacy Unencrypted Terminal Console)",
    80: "HTTP (Standard Cleartext Web Servers)",
    139: "NetBIOS (Windows File Sharing Access Service)",
    443: "HTTPS (Secure SSL Encrypted Web Servers)",
    3389: "RDP (Remote Desktop Protocol Protocol Gateway)"
}

print("\n=========================================")
print(f"🔒 RUNNING COMPREHENSIVE MULTI-THREADED SCAN")
print(f"Target Infrastructure Matrix : {TARGET_HOST}")
print(f"Scan Initialized On Timeline: {datetime.now()}")
print("=========================================\n")

# Thread lock configuration to keep terminal outputs neat and aligned
print_lock = threading.Lock()
open_ports_found = 0

def audit_port(port, service_name):
    global open_ports_found
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5) # Stable connection wait barrier threshold
    
    result = s.connect_ex((TARGET_HOST, port))
    
    with print_lock:
        if result == 0:
            print(f"⚠️  ALERT: Port {port} is OPEN | Vector: {service_name}")
            open_ports_found += 1
        else:
            print(f"🔒 Secure: Port {port} is closed/filtered.")
    s.close()

# --- OPTION 3: SPEED DEPLOYMENT VIA PARALLEL MULTI-THREADING ---
threads = []
for port_num, service_desc in PORTS_TO_SCAN.items():
    # Spawn a clean concurrent engine track for every individual port mapping target
    t = threading.Thread(target=audit_port, args=(port_num, service_desc))
    threads.append(t)
    t.start()

# Wait for all background parallel scans to cleanly sync back up and finish
for t in threads:
    t.join()

print("\n=========================================")
print("📈 SYSTEM SECURITY INVENTORY AUDIT COMPLETE")
print("=========================================")
print(f"Total Critical Service Vectors Checked: {len(PORTS_TO_SCAN)}")
print(f"Total Potentially Exposed Open Ports   : {open_ports_found}")
print("=========================================\n")
