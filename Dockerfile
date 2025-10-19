# Dockerfile - builds a small image for the Flask system monitor
FROM python:3.11-slim

# install build deps for psutil if necessary
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential gcc python3-dev libffi-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy requirements & install first (better cache)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# ensure start script is executable
RUN chmod +x /app/start.sh

# Port the app listens on
EXPOSE 5000

# default command
CMD ["/app/start.sh"]
