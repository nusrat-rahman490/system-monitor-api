import psutil
import json
import time
import os

# Log file path
LOG_FILE = os.environ.get("LOG_FILE", "/app/system_log.txt")

def get_stats():
    """Collect CPU, memory, and disk usage."""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - psutil.boot_time()))
    return {
        "cpu_usage": f"{cpu}%",
        "memory_usage": f"{memory}%",
        "disk_usage": f"{disk}%",
        "uptime": uptime,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

# Continuous logging
while True:
    data = get_stats()
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
    print("Logged:", data)
    time.sleep(5)  # Log every 5 seconds
