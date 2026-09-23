import sqlite3

print("=========================================")
print("📋 PARSING WORKSPACE DATABASE HISTORY")
print("=========================================\n")

DB_FILE = "workspace_telemetry.db"

try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Fetch all saved historical transaction records
    cursor.execute("SELECT id, timestamp, file_count, total_storage FROM system_logs ORDER BY id ASC")
    rows = cursor.fetchall()

    print(f"{'Log ID':<8}{'Timestamp Recorded':<24}{'File Count':<14}{'Directory Size':<15}")
    print("-" * 61)

    for row in rows:
        print(f"#{row[0]:<7}{row[1]:<24}{row[2]:<14}{row[3]:<5} Bytes")

    conn.close()
except Exception as e:
    print(f"❌ Database Query Interrupted: {e}")

print("\n=========================================")
