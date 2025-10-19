#!/usr/bin/env bash
# start.sh - run the app with gunicorn for production
# make sure script is executable: chmod +x start.sh

# Use 1 worker (simple). For production increase as needed (2x CPU cores + 1)
exec gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 1 --threads 4 "app:app"
