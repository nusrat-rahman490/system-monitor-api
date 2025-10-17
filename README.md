# 🖥️ System Monitor API

The **System Monitor API** is a lightweight monitoring tool built using **Python**, **Flask**, and **Docker**.  
It continuously tracks your system’s **CPU**, **memory**, **disk usage**, and **uptime**, logs them in real time, and exposes this data through a RESTful API.

This project demonstrates the integration of **Flask**, **psutil**, and **Docker** to create a simple, containerized monitoring service that can run locally or in a production environment.

---

## 🧠 Project Overview

The **System Monitor API** collects system metrics periodically using `psutil`, logs them into a text file, and provides easy-to-access API endpoints to retrieve the data.  

It is designed to:
- Demonstrate Python-based system monitoring.
- Show how to serve dynamic data using Flask.
- Use Docker for deployment and containerization.
- Log and serve real-time system performance information.

---

## ⚙️ Tech Stack

**Languages & Frameworks**
- 🐍 Python 3.10+
- 🌐 Flask 3.1.2 (Web Framework)
- ⚙️ psutil 7.1.0 (System Monitoring)

**DevOps & Tools**
- 🐳 Docker (Containerization)
- 📄 Shell Script (`start.sh`)
- 🔧 Git & GitHub (Version Control)

---

## 🧩 Project Structure
system-monitor-api/
│
├── app.py              # Flask API (serves system stats and logs)
├── monitor.py          # Background system logger (collects and writes stats)
├── requirements.txt    # Python dependencies
├── start.sh            # Startup script (runs monitor and Flask together)
├── Dockerfile          # Docker build instructions
└── README.md           # Project documentation

---

## ⚙️ How the Project Was Built

### 🧱 Environment Setup
- Created a Python virtual environment (`venv`)
- Installed Flask and psutil using pip

### 🧩 Backend Development
- Built **`app.py`** for REST API endpoints
- Created **`monitor.py`** to continuously log system stats every 5 seconds

### 🔗 Integration
- Combined both scripts with **`start.sh`** to run simultaneously

### 🐳 Containerization
- Wrote a **`Dockerfile`** to package the app into a Docker image  
- Exposed port **5000** for API access  
- Configured environment variables and entrypoints  

### 🧪 Testing
- Tested locally using Flask first  
- Then tested inside Docker container  
- Accessed the API via:
  - 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)
  - 👉 [http://localhost:5000](http://localhost:5000)

---

## 🚀 Features

✅ Monitors CPU, memory, disk usage, and uptime in real-time  
✅ Logs system metrics every few seconds  
✅ REST API to access live stats and log history  
✅ Runs both locally and inside Docker containers  
✅ Simple, modular, and extensible codebase  

---

## 🧪 API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Root endpoint with basic info |
| `/api/stats` | GET | Returns current CPU, memory, disk usage, and uptime |
| `/api/logs` | GET | Returns historical logs from `system_log.txt` |

### Example JSON Response from `/api/stats`
```json
{
  "cpu_usage": "13.2%",
  "memory_usage": "45.7%",
  "disk_usage": "68.1%",
  "uptime": "02:15:43"
}
