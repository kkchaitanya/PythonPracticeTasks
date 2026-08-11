# sms/manager.py

def validate_inputs(student_id, name, age, grade, email):
    """Validates all student input fields."""
    if not student_id or not str(student_id).strip():
        raise ValueError("Student ID cannot be empty.")
    if not name or not str(name).strip():
        raise ValueError("Name cannot be empty.")
    try:
        age_int = int(age)
        if age_int <= 0 or age_int > 150:
            raise ValueError("Age must be between 1 and 150.")
    except (TypeError, ValueError):
        raise ValueError("Age must be a valid integer.")
    if not grade or not str(grade).strip():
        raise ValueError("Grade cannot be empty.")
    if "@" not in str(email) or "." not in str(email):
        raise ValueError("Invalid email format.")


def get_student_by_id(students, student_id):
    """Returns a student dictionary by ID, or None."""
    for s in students:
        if s["id"] == student_id:
            return s
    return None


def add_student(students, student_id, name, age, grade, email, logger=None):
    """Adds a new student dictionary after validation."""
    try:
        validate_inputs(student_id, name, age, grade, email)
        if get_student_by_id(students, student_id):
            raise ValueError(f"Student ID {student_id} already exists.")
        students.append({
            "id": str(student_id).strip(),
            "name": str(name).strip(),
            "age": int(age),
            "grade": str(grade).strip(),
            "email": str(email).strip()
        })
        if logger:
            logger.info(f"Student added: ID={student_id}, Name={name}")
        return True
    except ValueError as ve:
        if logger:
            logger.warning(f"Add student failed: {ve}")
        print(f"Error: {ve}")
        return False


def remove_student(students, student_id, logger=None):
    """Removes a student by ID."""
    try:
        student = get_student_by_id(students, student_id)
        if not student:
            raise ValueError(f"Student ID {student_id} not found.")
        students.remove(student)
        if logger:
            logger.info(f"Student removed: ID={student_id}")
        return True
    except ValueError as ve:
        if logger:
            logger.warning(f"Remove student failed: {ve}")
        print(f"Error: {ve}")
        return False


def update_student(students, student_id, name=None, age=None, grade=None, email=None, logger=None):
    """Updates fields of an existing student."""
    try:
        student = get_student_by_id(students, student_id)
        if not student:
            raise ValueError(f"Student ID {student_id} not found.")
        if name is not None:
            student["name"] = str(name).strip()
        if age is not None:
            try:
                age_int = int(age)
                if age_int <= 0 or age_int > 150:
                    raise ValueError("Age must be between 1 and 150.")
                student["age"] = age_int
            except (TypeError, ValueError):
                raise ValueError("Age must be a valid integer.")
        if grade is not None:
            student["grade"] = str(grade).strip()
        if email is not None:
            if "@" not in str(email) or "." not in str(email):
                raise ValueError("Invalid email format.")
            student["email"] = str(email).strip()
        if logger:
            logger.info(f"Student updated: ID={student_id}")
        return True
    except ValueError as ve:
        if logger:
            logger.warning(f"Update student failed: {ve}")
        print(f"Error: {ve}")
        return False


def search_student(students, keyword, logger=None):
    """Searches students by ID, name, or email."""
    try:
        keyword = str(keyword).lower()
        results = [
            s for s in students
            if keyword in s["id"].lower()
            or keyword in s["name"].lower()
            or keyword in s["email"].lower()
        ]
        if logger:
            logger.info(f"Search '{keyword}' returned {len(results)} result(s).")
        return results
    except Exception as e:
        if logger:
            logger.error(f"Search error: {e}")
        return []


def display_all_students(students, logger=None):
    """Returns the list of all students (for display)."""
    if logger:
        logger.info(f"Displayed all students. Total: {len(students)}")
    return students


def format_student(student):
    """Returns formatted string for a single student."""
    return (f"ID: {student['id']} | Name: {student['name']} | "
            f"Age: {student['age']} | Grade: {student['grade']} | "
            f"Email: {student['email']}")


def student_to_file_format(student):
    """Returns pipe-delimited string for file storage."""
    return f"{student['id']}|{student['name']}|{student['age']}|{student['grade']}|{student['email']}"


def student_from_file_format(line):
    """Parses a line from the file into a student dictionary."""
    try:
        parts = line.strip().split("|")
        if len(parts) != 5:
            raise ValueError("Invalid data format")
        return {
            "id": parts[0],
            "name": parts[1],
            "age": int(parts[2]),
            "grade": parts[3],
            "email": parts[4]
        }
    except (ValueError, IndexError) as e:
        raise ValueError(f"Failed to parse student data: {e}")
