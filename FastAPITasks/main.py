from fastapi import FastAPI
from models.course import Course
# 1. Initialize the FastAPI application
app = FastAPI()

# 2. Define a root endpoint (GET request)
@app.get("/")
def read_root():
    return {"message": "Welcome to Super30 FastAPI"}


@app.get("/student")
def read_student():
    return {
             "name": "Sudhanshu",
             "batch": "Super30",
             "role": "Student"
            }

@app.get("/course")
def read_course():
    obj = Course(course_name="Backend Development with FastAPI",
                 mentor="Sudhanshu",
                 duration="8 Weeks",
                 topics=[
                        "Python",
                        "FastAPI",
                        "REST API",
                        "Database",
                        "Deployment"
                        ])
    return obj
            
@app.get("/skills")
def read_skills():
     return {
               "skills": [
                        "Python",
                        "FastAPI",
                        "SQL",
                        "Docker",
                        "AWS"
                        ]
                }


@app.get("/add/{a}/{b}")
def read_add(a: int, b: int ):
    return {"result":(a+b)}

@app.get("/multiply/{a}/{b}")
def read_multiply(a: int, b: int ):
    return {"result": (a*b)}

@app.get("/square/{number}")
def read_square(number: int ):
    return {
            "number": number,
            "square": (number**2)
            }

@app.get("/check/{number}")
def read_check(number: int ):
    return {
            "number": number,
            "square": "Even" if number % 2 == 0 else "Odd"
            }

@app.get("/age/{age}")
def read_check(age: int ):
    return {
            "age": age,
            "square": "Child" if age < 13 else "Teenager" if age < 20 else "Adult" if age < 65 else "Senior Citizen"
            }

@app.get("/table/{table_number}")
def read_check(table_number: int ):
    table_string=''
    for i in range(1, 11):
        result = table_number * i
        table_string = table_string+f"{table_number} x {i} = {result} "
    return {
            "table_number": table_number,
            "table":table_string
            }

@app.get("/profile/{name}/{age}")
def read_profile(name:str,age:int):
    return {
                "name": name,
                "age":age
        }
@app.get("/number/{number}")
def read_number_prop(number:int):
    return {
                    "number": number,
                    "square": number ** 2 ,
                    "cube": number **3,
                    "even": "even" if number%2 == 0  else "odd"
            }