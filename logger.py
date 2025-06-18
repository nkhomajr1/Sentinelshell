# core/logger.py
import json
from datetime import datetime
import os

LOG_FILE = "quarantine_log.json"

def log_quarantine(file_path, malware_name):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "file": file_path,
        "malware": malware_name
    }

    # Load existing log or start fresh
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)
