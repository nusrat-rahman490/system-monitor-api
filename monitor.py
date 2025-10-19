# monitor.py
# Background sampler: periodically collects system stats and keeps the latest sample.
import threading
import time
import psutil
from typing import Dict
from datetime import datetime
import threading

class SystemMonitor:
    def __init__(self, interval: int = 5):
        """
        interval: seconds between samples
        """
        self.interval = interval
        self._lock = threading.Lock()
        self._latest: Dict = {}
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def start(self):
        if not self._thread.is_alive():
            self._stop_event.clear()
            self._thread = threading.Thread(target=self._run, daemon=True)
            self._thread.start()

    def stop(self):
        self._stop_event.set()
        if self._thread.is_alive():
            self._thread.join(timeout=2)

    def _run(self):
        while not self._stop_event.is_set():
            sample = self._sample()
            with self._lock:
                self._latest = sample
            time.sleep(self.interval)

    def _sample(self) -> Dict:
        # Gather CPU
        cpu_percent = psutil.cpu_percent(interval=None)  # non-blocking current percent
        per_cpu = psutil.cpu_percent(interval=None, percpu=True)

        # Memory
        mem = psutil.virtual_memory()
        memory = {
            "total": mem.total,
            "available": mem.available,
            "used": mem.used,
            "free": mem.free,
            "percent": mem.percent
        }

        # Disk (root)
        disk = psutil.disk_usage("/")
        disk_info = {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        }

        ts = datetime.utcnow().isoformat() + "Z"
        return {
            "timestamp": ts,
            "cpu_percent": cpu_percent,
            "cpu_per_core": per_cpu,
            "memory": memory,
            "disk": disk_info
        }

    def get_latest(self) -> Dict:
        with self._lock:
            return dict(self._latest) if self._latest else {}

# Create a module-level monitor that other modules can import & start
monitor = SystemMonitor(interval=5)
