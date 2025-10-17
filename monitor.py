import psutil
import json
import time
import os

# Log file path
LOG_FILE = os.environ.get("LOG_FILE", "system_log.txt")

# Ensure file exists
os.makedirs(os.path.dirname(LOG_FILE) if os.path.dirname(LOG_FILE) else '.', exist_ok=True)
open(LOG_FILE, 'a').close()  # create empty file if not exists


def get_stats():
    """Collect CPU, memory, disk usage, and timestamp."""
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
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
    print("Logged:", data)
    time.sleep(5)  # every 5 seconds
