# sms/file_handler.py
import os
from .manager import student_to_file_format, student_from_file_format

def save_students(students, filename="students.txt", logger=None):
    """Writes all students to the file (overwrite mode)."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for student in students:
                f.write(student_to_file_format(student) + "\n")
        if logger:
            logger.info(f"Saved {len(students)} student(s) to file.")
    except (OSError, PermissionError) as e:
        if logger:
            logger.error(f"Failed to save file: {e}")
        raise


def load_students(filename="students.txt", logger=None):
    """Reads all students from the file."""
    students = []
    if not os.path.exists(filename):
        if logger:
            logger.warning("Data file not found. Starting with empty list.")
        return students

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                if line.strip():
                    try:
                        students.append(student_from_file_format(line))
                    except ValueError as ve:
                        if logger:
                            logger.error(f"Skipping line {line_num}: {ve}")
        if logger:
            logger.info(f"Loaded {len(students)} student(s) from file.")
        return students
    except (OSError, PermissionError) as e:
        if logger:
            logger.error(f"Failed to load file: {e}")
        raise
