from fastapi import FastAPI
import socket
app = FastAPI()
students = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Priya"},
    {"id": 3, "name": "Amit"}
]
@app.get("/students")
def get_students():
    return {
        "pod": socket.gethostname(),
        "students": students
    }
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": "Student not found"}