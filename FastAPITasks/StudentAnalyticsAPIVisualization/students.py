import numpy as np
students = [
    {"student_id": 1, "name": "Aarav Sharma", "python": 88, "mathematics": 92, "data_science": 90},
    {"student_id": 2, "name": "Priya Reddy", "python": 95, "mathematics": 89, "data_science": 94},
    {"student_id": 3, "name": "Rahul Kumar", "python": 76, "mathematics": 81, "data_science": 79},
    {"student_id": 4, "name": "Sneha Patel", "python": 91, "mathematics": 87, "data_science": 93},
    {"student_id": 5, "name": "Arjun Mehta", "python": 84, "mathematics": 78, "data_science": 86},
    {"student_id": 6, "name": "Ananya Singh", "python": 97, "mathematics": 95, "data_science": 96},
    {"student_id": 7, "name": "Vikram Rao", "python": 69, "mathematics": 74, "data_science": 71},
    {"student_id": 8, "name": "Kavya Nair", "python": 89, "mathematics": 91, "data_science": 88},
    {"student_id": 9, "name": "Rohan Gupta", "python": 73, "mathematics": 68, "data_science": 75},
    {"student_id": 10, "name": "Ishita Verma", "python": 92, "mathematics": 94, "data_science": 91},
    {"student_id": 11, "name": "Aditya Joshi", "python": 81, "mathematics": 85, "data_science": 83},
    {"student_id": 12, "name": "Meera Iyer", "python": 96, "mathematics": 90, "data_science": 95},
    {"student_id": 13, "name": "Karan Malhotra", "python": 64, "mathematics": 72, "data_science": 68},
    {"student_id": 14, "name": "Diya Kapoor", "python": 87, "mathematics": 86, "data_science": 89},
    {"student_id": 15, "name": "Nikhil Das", "python": 78, "mathematics": 80, "data_science": 77},
    {"student_id": 16, "name": "Sanya Kapoor", "python": 93, "mathematics": 96, "data_science": 94},
    {"student_id": 17, "name": "Manish Yadav", "python": 71, "mathematics": 66, "data_science": 70},
    {"student_id": 18, "name": "Pooja Shah", "python": 85, "mathematics": 88, "data_science": 84},
    {"student_id": 19, "name": "Dev Menon", "python": 90, "mathematics": 83, "data_science": 87},
    {"student_id": 20, "name": "Neha Agarwal", "python": 94, "mathematics": 92, "data_science": 93}
]

# --------------------------------------------------
# Helper function
# --------------------------------------------------

def get_overall_average(student):
    marks = [
        student["python"],
        student["mathematics"],
        student["data_science"]
    ]
    return round(float(np.mean(marks)), 2)