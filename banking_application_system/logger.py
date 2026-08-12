# sms/logger_setup.py
import logging

def setup_logger(log_file="logs/banking_application_system.log"):
    """
    Configures and returns a logger that writes to log_file.
    Log format: timestamp - level - message
    """
    try:
        logger = logging.getLogger("ExpenseTrackerSystem")
        logger.setLevel(logging.INFO)

        # Avoid duplicate handlers if function is called multiple times
        if logger.handlers:
            return logger

        # File handler
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.info("Logger initialized successfully.")
        return logger

    except (OSError, PermissionError) as e:
        print(f"Failed to setup logger: {e}")
        raise
