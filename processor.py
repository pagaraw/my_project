import os
from datetime import datetime

print("=========================================")
print("📊 EXECUTING FILE STORAGE METRIC PARSER")
print("=========================================\n")

total_bytes = 0
file_count = 0

for i in range(1, 11):
    filename = f"project{i}.txt"

    if os.path.exists(filename):
        file_count += 1
        size_bytes = os.path.getsize(filename)
        total_bytes += size_bytes

        print(f"✔️ Scanning: {filename} | Footprint: {size_bytes} Bytes")

        with open(filename, "a") as file:
            file.write(f"--- PARSER LOG METRIC ---\nSize Validation: {size_bytes}B\nLogged At: {datetime.now()}\n-------------------------\n\n")
    else:
        print(f"❌ Error: {filename} not located.")

print("\n=========================================")
print("📈 FINAL ANALYTICS OVERVIEW REPORT")
print("=========================================")
print(f"Total Operational Modules Tracking : {file_count}")
print(f"Total Structural Storage Footprint: {total_bytes} Bytes")
if file_count > 0:
    print(f"Average Storage Allocation Unit : {round(total_bytes / file_count, 2)} Bytes")
print("=========================================\n")
