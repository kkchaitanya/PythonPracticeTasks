from fastapi import FastAPI,Request
from flask import jsonify
from students import students,get_overall_average
import numpy as np
import plotly.graph_objects as go
from fastapi.templating import Jinja2Templates

# 1. Initialize the FastAPI application
app = FastAPI()

students_list = students
templates = Jinja2Templates(directory="templates")

@app.get("/students")
def read_students():
    return students_list

@app.get("/student/{student_id}")
def read_add(student_id: int ):
    return students_list[student_id]

@app.get("/average/python")
def read_add(student_id: int ):
    marks = np.array([student["python"] for student in students])
    return {
        "subject": "Python",
        "average": round(float(np.mean(marks)), 2)
        }

@app.get("/average/mathematics")
def read_add(student_id: int ):
    marks = np.array([student["mathematics"] for student in students])
    return {
        "subject": "mathematics",
        "average": round(float(np.mean(marks)), 2)
        }

@app.get("/average/data-science")
def read_add(student_id: int ):
    marks = np.array([student["data_science"] for student in students])
    return {
        "subject": "data-science",
        "average": round(float(np.mean(marks)), 2)
        }

@app.get("/passed")
def passed_students():
    passed = []
    for student in students:
        average = get_overall_average(student)
        if (
            student["python"] >= 40
            and student["mathematics"] >= 40
            and student["data_science"] >= 40
            and average >= 50
        ):
            result = student.copy()
            result["overall_average"] = average
            passed.append(result)
    return passed

@app.get("/failed")
def failed_students():
    failed = []
    for student in students:
        average = get_overall_average(student)
        if (
            student["python"] < 40
            or student["mathematics"] < 40
            or student["data_science"] < 40
            or average < 50
        ):
            result = student.copy()
            result["overall_average"] = average
            failed.append(result)
    return failed

@app.get("/topper")
def topper():
    top_student = max(
        students,
        key=get_overall_average
    )
    result = top_student.copy()
    result["overall_average"] = get_overall_average(top_student)
    return result

@app.get("/statistics")
def statistics():
    python_marks = np.array([marks["python"] for marks in students])
    mathematics = np.array([marks["mathematics"] for marks in students])
    data_science = np.array([marks["data_science"] for marks in students])

    return {
        # Subject averages
        "subject_averages": {
            "python": float(np.mean(python_marks)),
            "mathematics": float(np.mean(mathematics)),
            "data_science": float(np.mean(data_science))
        },

        # Highest marks
        "highest_marks": {
            "python": int(np.max(python_marks)),
            "mathematics": int(np.max(mathematics)),
            "data_science": int(np.max(data_science))
        },

        # Lowest marks
        "lowest_marks": {
            "python": int(np.min(python_marks)),
            "mathematics": int(np.min(mathematics)),
            "data_science": int(np.min(data_science))
        },

        # Overall average
        "overall_average": float(
            np.mean(
                np.concatenate([
                    python_marks,
                    mathematics,
                    data_science
                ])
            )
        )
    }

# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# import numpy as np
# import plotly.graph_objects as go

# app = FastAPI()

# templates = Jinja2Templates(directory="templates")


@app.get("/plot/subjects")
def subject_plot(request: Request):

    subjects_names = [
        "Python",
        "Mathematics",
        "Data Science"
    ]

    averages = [
        np.mean([student["python"] for student in students]),
        np.mean([student["mathematics"] for student in students]),
        np.mean([student["data_science"] for student in students])
    ]

    fig = go.Figure(
        data=[
            go.Bar(
                x=subjects_names,
                y=averages,
                marker_color=["#3776AB", "#F2C14E", "#4CAF50"],
                text=[round(value, 2) for value in averages],
                textposition="auto"
            )
        ]
    )

    fig.update_layout(
        title="Average Marks Across Subjects",
        xaxis_title="Subject",
        yaxis_title="Average Marks",
        yaxis=dict(range=[0, 100])
    )

    return templates.TemplateResponse(
        "subject_averages.html",
        {
            "request": request,
            "plot": fig.to_html(full_html=False)
        }
    )


@app.get("/plot/top-five")
def top_five_plot(request: Request):

    sorted_students = sorted(
        students,
        key=get_overall_average,
        reverse=True
    )

    top_five = sorted_students[:5]

    names = [student["name"] for student in top_five]

    averages = [
        get_overall_average(student)
        for student in top_five
    ]

    fig = go.Figure(
        data=[
            go.Bar(
                x=names,
                y=averages,
                marker_color="#636EFA",
                text=averages,
                textposition="auto"
            )
        ]
    )

    fig.update_layout(
        title="Top Five Students by Overall Average",
        xaxis_title="Student",
        yaxis_title="Overall Average",
        yaxis=dict(range=[0, 100])
    )

    return templates.TemplateResponse(
        "top_five.html",
        {
            "request": request,
            "plot": fig.to_html(full_html=False)
        }
    )
