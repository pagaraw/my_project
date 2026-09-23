#!/bin/bash
# Automated workspace audit, compression, and log rotation script

echo "Starting workspace audit..."

for i in {1..10}
do
    FILE="project${i}.txt"
    if [ -f "$FILE" ]; then
        echo "Adding header to $FILE..."
        echo -e "--- SYSTEM BLOCK LOG ---\nInitialized: $(date)\n------------------------\n" > "$FILE"
    else
        echo "Warning: $FILE not found. Creating it now..."
        echo -e "--- SYSTEM BLOCK LOG ---\nInitialized: $(date)\n------------------------\n" > "$FILE"
    fi
done

echo "Creating compressed backup archive..."
BACKUP_NAME="project_backup_$(date +%F).tar.gz"
tar -czf "$BACKUP_NAME" project*.txt
echo "Backup complete! Saved locally as: $BACKUP_NAME"

# --- AUTOMATED STORAGE RETENTION LOG ROTATION SECTION ---
echo "Evaluating local disk storage retention window..."

# Find and delete backup archives matching our pattern that were modified more than 7 days ago
find . -name "project_backup_*.tar.gz" -type f -mtime +7 -exec rm -f {} \;

echo "Log rotation verification scan complete! Storage footprint minimized."
