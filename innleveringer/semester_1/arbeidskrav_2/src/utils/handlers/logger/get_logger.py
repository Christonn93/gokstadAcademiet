import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(
    name: str,
    level: int = logging.INFO,
    log_file: str = "app.log",
    max_bytes: int = 1_000_000,
    backup_count: int = 3
):
    log_instance = logging.getLogger(name)
    log_instance.setLevel(level)

    # Prevent adding multiple handlers if function is called multiple times
    if log_instance.handlers:
        return log_instance

    # ✅ Console handler (prints warnings and above to terminal)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter("📢 %(levelname)s - %(message)s")
    console_handler.setFormatter(console_format)

    # ✅ Rotating file handler (saves errors to a file, rotates logs)
    os.makedirs("logs", exist_ok=True)
    file_handler = RotatingFileHandler(
        os.path.join("logs", log_file),
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.ERROR)
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_format)

    # ✅ Attach handlers
    log_instance.addHandler(console_handler)
    log_instance.addHandler(file_handler)

    return log_instance


# Create logger for this file/module
logger = get_logger(__name__)
