# core/restorer.py
import json
import os
import shutil

QUARANTINE_DIR = "quarantine"
LOG_FILE = "quarantine_log.json"

def restore_file(filename):
    try:
        with open(LOG_FILE, "r") as f:
            entries = json.load(f)
    except FileNotFoundError:
        print("⚠️ No quarantine log found.")
        return

    # Find the most recent matching entry
    match = next((e for e in reversed(entries) if os.path.basename(e["file"]) == filename), None)
    if not match:
        print(f"❌ No record found for {filename}")
        return

    src = os.path.join(QUARANTINE_DIR, filename)
    dest = match["file"]

    if not os.path.exists(src):
        print(f"❌ Quarantined file not found: {src}")
        return

    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.move(src, dest)
    print(f"✅ Restored: {filename} → {dest}") 
