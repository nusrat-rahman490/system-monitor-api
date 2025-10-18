#!/bin/bash

# Start monitor.py in the background
python3 monitor.py &

# Start Flask on all interfaces
flask run --host=0.0.0.0 --port=5000
