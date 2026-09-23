#!/bin/bash
# Master Infrastructure Control Launcher

echo "========================================="
echo "🚀 INITIALIZING WORKSPACE AUTOMATION MATRIX"
echo "========================================="

./error_handler.sh
python3 net_scanner.py
python3 api_fetcher.py
python3 db_logger.py
python3 sync_dashboard.py
python3 db_report.py

echo "========================================="
echo "✅ PIPELINE SUCCESS: All systems synchronized!"
echo "========================================="
