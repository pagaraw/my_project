import urllib.request
import json
from datetime import datetime

print("=========================================")
print("🌐 EXECUTING INTERACTIVE DATA SCRAPER")
print("=========================================\n")

try:
    # Query a secure public API endpoint for localized network metadata
    url = "https://ipapi.co"
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)

    print("Querying secure external API endpoint protocols...")
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())

        ip = data.get("ip", "Unknown")
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        org = data.get("org", "Unknown")

        print(f"✔️ Extracted Public IP : {ip}")
        print(f"✔️ Detected Location   : {city}, {region}")
        print(f"✔️ Infrastructure ISP  : {org}")

        # Export the raw network analytics summary to a localized audit file
        with open("network_metadata.txt", "w") as f:
            f.write(f"=== PUBLIC INFRASTRUCTURE METADATA ===\n")
            f.write(f"Timestamp Logged : {datetime.now()}\n")
            f.write(f"Public IP Address: {ip}\n")
            f.write(f"Node Location    : {city}, {region}\n")
            f.write(f"Network Provider : {org}\n")
        print("\nMetrics cleanly exported to: network_metadata.txt")

except Exception as e:
    print(f"❌ API Query Interrupted: {e}")

print("\n=========================================")
