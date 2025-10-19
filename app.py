# app.py
from flask import Flask, jsonify
from monitor import monitor
import atexit

app = Flask(__name__)

@app.route("/api/stats", methods=["GET"])
def stats():
    """
    Return the latest system stats collected by the monitor.
    If monitor hasn't collected anything yet, collect one synchronously.
    """
    data = monitor.get_latest()
    # if empty (first request), force a synchronous sample
    if not data:
        # start monitor and give it one immediate sample
        monitor.start()
        # give a tiny moment for the monitor to collect (it's fast)
        import time
        time.sleep(0.1)
        data = monitor.get_latest()
    return jsonify(data)

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "System Resource Monitor API", "endpoint": "/api/stats"})

def _start_monitor():
    monitor.start()

def _stop_monitor():
    monitor.stop()

if __name__ == "__main__":
    # for local dev run: start monitor then run flask dev server
    _start_monitor()
    try:
        app.run(host="0.0.0.0", port=5000, debug=False)
    finally:
        _stop_monitor()

# Ensure monitor is stopped when process exits (useful for gunicorn reloads too)
atexit.register(_stop_monitor)
