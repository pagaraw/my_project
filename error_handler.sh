#!/bin/bash
# Automated Workspace Error Audit Handler

LOG_FILE="error_log.txt"
CRITICAL_FILES=("initialization.sh" "processor.py" "net_scanner.py" "dashboard.html")
errors_found=0

echo "Checking workspace configurations..."

for file in "${CRITICAL_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        error_msg="[CRITICAL ERROR] $(date) - Missing file element: $file"
        echo "$error_msg"
        echo "$error_msg" >> "$LOG_FILE"
        errors_found=$((errors_found + 1))
    fi
done

if [ $errors_found -eq 0 ]; then
    echo "🔒 Status Secure: Workspace integrity verified. 0 core file exceptions found."
else
    echo "⚠️ Warnings logged! Detailed diagnostic reports written to: $LOG_FILE"
fi
