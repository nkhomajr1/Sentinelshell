import argparse
import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core import scanner
from core.restorer import restore_file
from utils.theme import enable_ansi, banner
from utils.rain import matrix_rain
from playsound import playsound

def voice_greeting():
    try:
        playsound("assets/sentinel_greeting.wav")
    except:
        pass  # Silent fail if audio missing

def main():
    parser = argparse.ArgumentParser(description="SentinelShell Antivirus")
    parser.add_argument("target", nargs="?", default=None, help="Directory or file to scan")
    parser.add_argument("--quarantine", action="store_true", help="Quarantine detected threats")
    parser.add_argument("--restore", type=str, help="Restore a quarantined file")
    args = parser.parse_args()

    enable_ansi()
    matrix_rain(duration=2)
    voice_greeting()
    print(banner())

    if args.restore:
        restore_file(args.restore)
    elif args.target:
        scanner.scan_directory(args.target, quarantine=args.quarantine)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
