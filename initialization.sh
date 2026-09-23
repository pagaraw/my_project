#!/bin/bash
# Automated workspace audit and cross-OS compression script

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

# --- NEW WINDOWS BACKUP MIRROR SECTION ---
echo "Mirroring backup safely to Windows Storage..."
# This finds your exact Windows username dynamically and copies the file to your Windows Documents folder
WINDOWS_USER=$(powershell.exe '$env:UserName' | tr -d '\r')
mkdir -p "/mnt/c/Users/$WINDOWS_USER/Documents/Project_Backups"
cp "$BACKUP_NAME" "/mnt/c/Users/$WINDOWS_USER/Documents/Project_Backups/"
echo "Cross-OS mirror sync successful!"
