import os
import time

# === JUST FOR FUN AND GIGGLES ===
def elevator_music(duration=5):
    """Play elevator music in console with running animation."""
    runners = ["🧎‍♀️‍➡️", "🧎‍♂️‍➡️", "🧎‍➡️", "🚶‍♀️‍➡️", "🚶‍♂️‍➡️", "🚶‍➡️", "🏃‍♀️‍➡️", "🏃‍♂️‍➡️", "🏃‍➡️"]

    end_time = time.time() + duration
    i = 0

    while time.time() < end_time:
        runner = runners[i % len(runners)]
        print(f"\r{runner}", end="", flush=True)
        time.sleep(0.2)
        i += 1

    print(f"\r🏁", end="", flush=True)
    time.sleep(1)
    print()

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def styled_print(message, style=""):
    """Print styled messages."""
    styles = {
        "header": "\033[1;36m",      # Bold Cyan
        "success": "\033[1;32m",     # Bold Green
        "warning": "\033[1;33m",     # Bold Yellow
        "error": "\033[1;31m",       # Bold Red
        "info": "\033[1;34m",        # Bold Blue
        "reset": "\033[0m"           # Reset to default
    }
    print(f"{styles.get(style, '')}{message}{styles['reset']}")

def clear_and_header(header_text):
    """Clear console and print styled header."""
    clear_console()
    styled_print("=" * 50, "header")
    styled_print(header_text, "header")
    styled_print("=" * 50, "header")
    print()