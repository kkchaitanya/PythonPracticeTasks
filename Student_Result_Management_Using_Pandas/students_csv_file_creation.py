import pandas as pd

data = {
    "student_id": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,
                   1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,
                   1021,1022,1023,1024,1025],
    "name": ["Alice","Bob","Charlie","David","Eva","Frank","Grace","Henry",
             "Irene","Jack","Karen","Liam","Mia","Noah","Olivia","Peter",
             "Queen","Ryan","Sophia","Thomas","Thomas","Thomas","Thomas","Thomas","Thomas"],
    "age": [21,22,20,23,21,22,20,21,23,22,20,21,22,23,20,21,22,23,20,21,21,22,23,20,21],
    "city": ["Hyderabad","Mumbai","Bangalore","Chennai","Pune","Delhi",
             "Kolkata","Hyderabad","Mumbai","Bangalore","Chennai","Pune",
             "Delhi","Kolkata","Hyderabad","Mumbai","Bangalore","Chennai",
             "Pune","Delhi","Pune","Delhi","Pune","Delhi","Chennai"],
    "python_marks": [85,72,90,65,88,55,93,78,84,69,91,74,87,62,95,70,82,58,89,77,70,82,58,89,77],
    "sql_marks": [78,68,85,70,91,60,89,82,79,72,88,76,90,65,93,74,86,55,87,80,74,86,55,87,80],
    "pandas_marks": [82,75,89,68,87,58,95,80,81,70,92,73,85,67,96,72,84,60,90,78,72,84,60,90,78],
    "attendance": [92,88,95,80,96,75,98,90,87,85,97,89,94,78,99,84,91,72,95,88,84,91,72,95,88]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

print("students.csv created successfully!")