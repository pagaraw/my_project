#!/bin/bash
# Master Infrastructure Control Launcher

echo "========================================="
echo "🚀 INITIALIZING WORKSPACE AUTOMATION MATRIX"
echo "========================================="

# 1. Execute your parallel multi-threaded network security scanning engine
python3 net_scanner.py

# 2. Trigger your interactive public network API metadata data scraper
python3 api_fetcher.py

# 3. Commit current transaction block variables into your SQLite Database file
python3 db_logger.py

# 4. Run your synchronized metrics updater to push variables to dashboard.html
python3 sync_dashboard.py

echo "========================================="
echo "✅ PIPELINE SUCCESS: All engines executed and synced!"
echo "========================================="
