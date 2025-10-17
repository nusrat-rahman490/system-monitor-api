#!/bin/bash
# Start monitor.py in the background
python3 monitor.py &
# Start Flask
flask run --host=0.0.0.0
