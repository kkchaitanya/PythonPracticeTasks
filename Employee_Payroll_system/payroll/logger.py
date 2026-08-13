import logging
import os

os.makedirs("logs", exist_ok=True)

payroll_logger = logging.getLogger("payroll_logger")
payroll_logger.setLevel(logging.INFO)

payroll_handler = logging.FileHandler("logs/payroll.log")
payroll_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
payroll_logger.addHandler(payroll_handler)

error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)

error_handler = logging.FileHandler("logs/error.log")
error_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
error_logger.addHandler(error_handler)