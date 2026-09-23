import sqlite3

print("=========================================")
print("📈 GRAPHICAL WORKSPACE REPOSITORY MATRIX")
print("=========================================\n")

DB_FILE = "workspace_telemetry.db"

try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Fetch the last 5 operational records stored in your SQL rows
    cursor.execute("SELECT id, timestamp, total_storage FROM system_logs ORDER BY id DESC LIMIT 5")
    rows = sorted(cursor.fetchall()) # Order chronologically for the graph

    for row in rows:
        log_id, timestamp, storage_bytes = row

        # Convert byte sizes into relative string bar lengths for our terminal display chart
        bar_length = int(storage_bytes / 1000) if storage_bytes > 1000 else int(storage_bytes / 100)
        bar_visual = "█" * (bar_length if bar_length > 0 else 1)

        print(f"Log #{log_id} ({timestamp[:16]})")
        print(f"[{bar_visual:<35}] {storage_bytes} Bytes\n")

    conn.close()
except Exception as e:
    print(f"❌ Graph Engine Error: {e}")

print("=========================================")
