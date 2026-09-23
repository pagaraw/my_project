import socket
import threading
from datetime import datetime

print("=========================================")
print("🌐 ENHANCED NETWORK SERVICE AUDITOR")
print("=========================================\n")

BASE_NET = "127.0.0."
TARGET_PORTS = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS"}

print_lock = threading.Lock()
report_lines = []

def grab_banner(s):
    try:
        # Send a blank line or request payload to force the service to introduce itself
        s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        # Grab just the first line of the application's signature response block
        return banner.split('\n')[0] if banner else "Unknown Service Version"
    except:
        return "No response signature string extracted."

def audit_node(ip_address, port, service):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)

    result = s.connect_ex((ip_address, port))

    with print_lock:
        if result == 0:
            signature = grab_banner(s)
            alert = f"⚠️ ALERT: Host {ip_address} | Port {port} ({service}) is OPEN\n   --> System Signature: {signature}"
            print(alert)
            report_lines.append(alert)
    s.close()

threads = []
print(f"Commencing parallel banner grabbing audit across local scope...\n")

for host_id in range(1, 3):
    target_ip = f"{BASE_NET}{host_id}"
    for port_num, service_desc in TARGET_PORTS.items():
        t = threading.Thread(target=audit_node, args=(target_ip, port_num, service_desc))
        threads.append(t)
        t.start()

for t in threads:
    t.join()
