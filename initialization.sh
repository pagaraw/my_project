#!/bin/bash
# A simple automation script to initialize your 10 project files

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
