import os, json, time
import psutil
from flask import Flask, jsonify

app = Flask(__name__)

# LOG_FILE: container default /app/system_log.txt,
# overridden by environment if set (useful for local testing)
LOG_FILE = os.environ.get("LOG_FILE", "/app/system_log.txt")

@app.route('/api/stats', methods=['GET'])
def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - psutil.boot_time()))
    stats = {
        "cpu_usage": f"{cpu}%",
        "memory_usage": f"{memory}%",
        "disk_usage": f"{disk}%",
        "uptime": uptime
    }
    return jsonify(stats)

@app.route('/api/logs', methods=['GET'])
def get_logs():
    logs = []
    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                line=line.strip()
                if line:
                    logs.append(json.loads(line))
    except FileNotFoundError:
        return jsonify({"error": "system_log.txt not found", "path": LOG_FILE}), 404
    return jsonify(logs)

@app.route('/')
def home():
    return "System Monitor API — use /api/stats and /api/logs"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
