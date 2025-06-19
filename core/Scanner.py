import hashlib, os, shutil, json, argparse
from datetime import datetime

SIGNATURE_DB = "signatures/malware_db.json"
QUARANTINE_DIR = "quarantine"
LOG_FILE = "quarantine_log.json"

class AntivirusScanner:
    def __init__(self, signature_db=SIGNATURE_DB, quarantine_dir=QUARANTINE_DIR, log_file=LOG_FILE):
        self.signature_db = signature_db
        self.quarantine_dir = quarantine_dir
        self.log_file = log_file
        self.signatures = self.load_signatures()

    def load_signatures(self):
        try:
            with open(self.signature_db, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def hash_file(self, path):
        try:
            with open(path, "rb") as f:
                return hashlib.sha256(f.read()).hexdigest()
        except:
            return None

    def log_threat(self, file_path, malware_name):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "file": file_path,
            "malware": malware_name
        }
        try:
            with open(self.log_file, "r") as f:
                data = json.load(f)
        except:
            data = []
        data.append(entry)
        with open(self.log_file, "w") as f:
            json.dump(data, f, indent=2)

    def quarantine_file(self, path):
        os.makedirs(self.quarantine_dir, exist_ok=True)
        dest = os.path.join(self.quarantine_dir, os.path.basename(path))
        shutil.move(path, dest)
        return dest

    def scan_directory(self, directory, quarantine=False):
        for root, _, files in os.walk(directory):
            for name in files:
                full_path = os.path.join(root, name)
                file_hash = self.hash_file(full_path)
                if file_hash in self.signatures:
                    print(f"[!] Threat Detected: {name} → {self.signatures[file_hash]}")
                    self.log_threat(full_path, self.signatures[file_hash])
                    if quarantine:
                        self.quarantine_file(full_path)
                        print(f"    ↳ Quarantined: {full_path}")
                else:
                    print(f"[OK] {name}")

# ───────────────────────────────────────
# CLI CORE
# ───────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Simple Antivirus Scanner")
    parser.add_argument("directory", help="Target directory to scan")
    parser.add_argument("-q", "--quarantine", action="store_true", help="Quarantine detected files")

    args = parser.parse_args()
    if not os.path.isdir(args.directory):
        print(f"❌ Error: Directory not found - {args.directory}")
        return

    scanner = AntivirusScanner()
    print(f"🔍 Scanning directory: {args.directory}")
    scanner.scan_directory(args.directory, quarantine=args.quarantine)

if __name__ == "__main__":
    main()
