#!/bin/bash
# Disaster Recovery Script for Automated Workspace

echo "========================================="
echo "⚠️ RUNNING DISASTER RECOVERY FAILOVER"
echo "========================================="

# Find the most recent backup archive file automatically
LATEST_BACKUP=$(ls -t project_backup_*.tar.gz 2>/dev/null | head -n 1)

if [ -z "$LATEST_BACKUP" ]; then
    echo "❌ Error: No backup archive file found! Cannot proceed with restore."
    exit 1
fi

echo "Found latest archive package: $LATEST_BACKUP"
echo "Purging old/corrupted local text instances..."

# Clear out the text files safely to ensure no partial corruptions remain
rm -f project*.txt

echo "Extracting clean source blocks out of archive backup..."
tar -xzf "$LATEST_BACKUP"

if [ $? -eq 0 ]; then
    echo "========================================="
    echo "✅ RECOVERY SUCCESSFUL: Project assets restored!"
    echo "========================================="
    ls -l project*.txt
else
    echo "❌ Error: Archive extraction failed midway."
fi
