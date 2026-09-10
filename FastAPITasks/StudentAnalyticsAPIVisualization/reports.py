from students import students,get_overall_average
import numpy as np
import plotly.graph_objects as go

def subject_plot():

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
    fig.show(renderer="browser")


def top_five_plot():

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
    fig.show(renderer="browser")

subject_plot()
top_five_plot()

 
