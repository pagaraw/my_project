import socket
from datetime import datetime

# Set the target to your local loopback address for a safe internal sandbox test
TARGET_HOST = "127.0.0.1"

# A list of standard common industry ports to audit for vulnerabilities
PORTS_TO_SCAN = {
    21: "FTP (File Transfer Protocol - Weak Security)",
    22: "SSH (Secure Shell Access Channel)",
    23: "Telnet (Unencrypted Cleartext - High Risk)",
    80: "HTTP (Standard Web Server Traffic)",
    443: "HTTPS (Secure Encrypted Web Server Traffic)",
    3389: "RDP (Remote Desktop Protocol Access Open)"
}

print("=========================================")
print(f"🔒 INITIALIZING CORE NETWORK SECURITY AUDIT")
print(f"Target Host Location: {TARGET_HOST}")
print(f"Scan Commenced At   : {datetime.now()}")
print("=========================================\n")

open_ports_found = 0

for port, service in PORTS_TO_SCAN.items():
    # Establish a clean TCP socket streaming connection block
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a fast 1-second timeout so the scan doesn't hang on closed doors
    s.settimeout(1.0)
    
    # Attempt to connect to the target port
    result = s.connect_ex((TARGET_HOST, port))
    
    if result == 0:
        print(f"⚠️  ALERT: Port {port} is OPEN | Service: {service}")
        open_ports_found += 1
    else:
        print(f"🔒 Secure: Port {port} is closed or filtered.")
        
    s.close()

print("\n=========================================")
print("📈 SYSTEM SECURITY INVENTORY AUDIT COMPLETE")
print("=========================================")
print(f"Total Critical Service Vectors Checked: {len(PORTS_TO_SCAN)}")
print(f"Total Potentially Exposed Open Ports   : {open_ports_found}")
print("=========================================\n")
