# launcher.py
import argparse
from core import scanner
from core.restorer import restore_file
from utils.theme import enable_ansi, banner
from utils.rain import matrix_rain
from playsound import playsound  # Optional: for voice greeting

def voice_greeting():
    try:
        playsound("assets/sentinel_greeting.wav")
    except:
        pass  # Fail silently if audio is missing

def main():
    parser = argparse.ArgumentParser(description="SentinelShell Antivirus")
    parser.add_argument("target", nargs="?", default=None, help="Path to scan")
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
        print("Usage:")
        print("  python launcher.py <path> [--quarantine]")
        print("  python launcher.py --restore <filename>")

if __name__ == "__main__":
    main()
 