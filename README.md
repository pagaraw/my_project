# 🛠️ Automated File Audit & Backup Workspace

A native Linux automation project hosted inside Ubuntu WSL, featuring automated file initialization, state logging, and compressed tracking.

## 🚀 Features
* **Batch Initialization:** Automatically audits `project1.txt` through `project10.txt` and appends localized system timestamps.
* **Automated Archiving:** Compresses active assets into localized `.tar.gz` packages.
* **Scheduled Execution:** Configured via Linux system `cron` to capture workspace snapshots daily at midnight.
* **Git Hygiene:** Utilizes optimized `.gitignore` protocols to isolate source code from binary storage.

## 🔧 Project Structure
* `initialization.sh` - Core Bash automation script.
* `.gitignore` - Rule mapping to exclude compressed tarball files.
* `project*.txt` - Targeted workspace data modules.
