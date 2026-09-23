#!/bin/bash
# Automated workspace audit and compression script

echo "Starting workspace audit..."

# Loop through files 1 to 10
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

echo "Workspace successfully initialized!"

# --- NEW AUTOMATED BACKUP SECTION ---
echo "Creating compressed backup archive..."
BACKUP_NAME="project_backup_$(date +%F).tar.gz"

# Compress all 10 project text files into one archive
tar -czf "$BACKUP_NAME" project*.txt

echo "Backup complete! Saved as: $BACKUP_NAME"
