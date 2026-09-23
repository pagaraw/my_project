import os
import sqlite3
from datetime import datetime

print("=========================================")
print("💾 INITIALIZING INTERNAL SQLITE DATABASE")
print("=========================================\n")

# Define file target footprints
DB_FILE = "workspace_telemetry.db"

# Establish connection to the local database file system
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Initialize a structured repository telemetry mapping log table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS system_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        file_count INTEGER NOT NULL,
        total_storage INTEGER NOT NULL
    )
''')

# Gather actual file inventory parameters dynamically
total_bytes = 0
file_count = 0
for file in os.listdir("."):
    if file.endswith(".txt") or file.endswith(".sh") or file.endswith(".py") or file.endswith(".html"):
        file_count += 1
        total_bytes += os.path.getsize(file)

# Inject a structured real-time transaction record directly into the database row arrays
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cursor.execute('''
    INSERT INTO system_logs (timestamp, file_count, total_storage)
    VALUES (?, ?, ?)
''', (current_time, file_count, total_bytes))

# Commit data blocks and close standard connection pipelines safely
conn.commit()
print("✔️ Relational transaction block successfully committed to database storage matrix.")

# Query the historical database table to verify logs are mapping correctly
print("\nParsing current historical timeline logs from data tables:")
cursor.execute("SELECT * FROM system_logs ORDER BY id DESC LIMIT 3")
records = cursor.fetchall()

for row in records:
    print(f" > Record #{row[0]} | Date: {row[1]} | Assets: {row[2]} | Storage Size: {row[3]}B")

conn.close()
print("\n=========================================")
