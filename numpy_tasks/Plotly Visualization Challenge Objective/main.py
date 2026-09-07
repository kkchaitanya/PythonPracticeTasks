import plotly.express as px
import numpy as np
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 140, 200, 230]

fig = px.bar(
    x=months,
    y=sales,
    labels={
        "x": "Months",
        "y": "Sales"
    },
    title="Monthly Sales"
)

fig.show(renderer="browser")

fig1 = px.line(
    x=months,
    y=sales,
    labels={
        "x": "Months",
        "y": "Sales"
    },
    markers=True,
    title="Monthly Sales"
)

fig1.show(renderer="browser")


departments = ["Engineering", "Sales", "Marketing", "HR", "Operations"]
employees = [40, 25, 15, 10, 10]

fig2 = px.pie(
    names=departments,
    values=employees,
    title="Department-wise Employee Distribution"
)

fig2.show(renderer="browser")


hours_studied = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10]
exam_marks = [35, 40, 45, 50, 52, 58, 62, 65, 68, 72, 75, 78, 84, 88, 95]

scatter = px.scatter(
    x=hours_studied,
    y=exam_marks,
    title="Hours Studied vs Exam Marks",
    labels={
        "x": "Hours Studied",
        "y": "Exam Marks"
    }
)

scatter.show(renderer="browser")

##Histogram
histogram = px.histogram(
    x=hours_studied,
    y=exam_marks,
    title="Hours Studied vs Exam Marks",
    labels={
        "x": "Hours Studied",
        "y": "Exam Marks"
    }
)
histogram.show(renderer="browser")



# Generate 500 random values 
data = np.random.randn(500)
# Create histogram 
histogram = px.histogram(
                         x=data, 
                         nbins=20, 
                         title="Histogram of 500 Random Values", 
                         labels={ "x": "Random Values", "y": "Frequency" } ) 
fig.show(renderer="browser")


# Salary information for 30 employees 
salaries = [ 25000, 28000, 30000, 32000, 35000, 36000, 38000, 40000, 42000, 45000, 46000, 48000, 50000, 52000, 55000, 56000, 58000, 60000, 62000, 65000, 68000, 70000, 
            72000, 75000, 80000, 85000, 90000, 95000, 100000, 120000 ] 
salaries = px.box( y=salaries, title="Salary Distribution of 30 Employees",
                   labels={ "y": "Salary" } ) 
fig.show(renderer="browser")


# Student Performance
# Create marks for 10 students in
# Python
# Mathematics
# Data Science

import plotly.graph_objects as go

students = [
    "Student 1", "Student 2", "Student 3", "Student 4", "Student 5",
    "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"
]

python_marks = [85, 78, 92, 70, 88, 95, 76, 84, 90, 82]
math_marks = [80, 75, 89, 72, 85, 91, 79, 88, 86, 81]
data_science_marks = [88, 82, 94, 75, 90, 96, 80, 86, 92, 85]

fig = go.Figure()

fig.add_trace(go.Bar(
    x=students,
    y=python_marks,
    name="Python"
))

fig.add_trace(go.Bar(
    x=students,
    y=math_marks,
    name="Mathematics"
))

fig.add_trace(go.Bar(
    x=students,
    y=data_science_marks,
    name="Data Science"
))

fig.update_layout(
    title="Student Performance",
    xaxis_title="Students",
    yaxis_title="Marks",
    barmode="group"
)

fig.show(renderer="browser")


