import socket
import threading
from datetime import datetime

print("=========================================")
print("🌐 SUBNET NETWORK ARCHITECTURE SCANNER")
print("=========================================\n")

# Base network subnet mask block to evaluate
BASE_NET = "127.0.0."
# Critical core ports index mapping to common technical vectors
TARGET_PORTS = {22: "SSH", 80: "HTTP", 443: "HTTPS"}

print_lock = threading.Lock()
scanned_nodes = 0
exposed_vectors = 0
report_lines = []

def audit_node(ip_address, port, service):
    global exposed_vectors
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Fast scanning barrier threshold

    result = s.connect_ex((ip_address, port))

    with print_lock:
        if result == 0:
            alert = f"⚠️ ALERT: Host {ip_address} has open entry vector on Port {port} ({service})"
            print(alert)
            report_lines.append(alert)
            exposed_vectors += 1
    s.close()

threads = []
print(f"Commencing parallel multi-threaded block sweep across node scope 127.0.0.1 - 127.0.0.5...\n")

# Loop through an array block of 5 sequential server IP targets simultaneously
for host_id in range(1, 6):
    target_ip = f"{BASE_NET}{host_id}"
    scanned_nodes += 1

    for port_num, service_desc in TARGET_PORTS.items():
        t = threading.Thread(target=audit_node, args=(target_ip, port_num, service_desc))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

# Automatically output and format your diagnostic matrix report
with open("scan_report.txt", "w") as f:
    f.write(f"=== MULTI-NODE SUBNET SECURITY AUDIT REPORT ===\n")
    f.write(f"Timestamp Logged : {datetime.now()}\n")
    f.write(f"Total Nodes Polled : {scanned_nodes}\n")
    f.write(f"Open Service Risks Found: {exposed_vectors}\n")
    f.write("-----------------------------------------------\n")
    if report_lines:
        for line in report_lines: f.write(f"{line}\n")
    else:
        f.write("🔒 Status Secure: No open service vulnerabilities detected across target subnet.\n")

print("\n=========================================")
print(f"📈 SUBNET SWEEP AUDIT COMPLETE | Nodes Tracked: {scanned_nodes}")
print("Exported aggregated metrics matrix to: scan_report.txt")
print("=========================================\n")
