import pandas as pd

df = pd.read_csv("students.csv")

print(df.head()) # First 5 rows
print(df.tail()) # Last 5 rows
print(df.shape) # Rows and columns count
print(df.columns) # All columns
print(df.info())
print(df.describe())

#Find average Python marks.
print(f"average python_marks : {df['python_marks'].mean()}")
#Find average SQL marks.
print(f"average sql_marks : {df['sql_marks'].mean()}")
#Find average Pandas marks.
print(f"average pandas_marks: {df['pandas_marks'].mean()}")

#Find maximum marks.
print(f"Max Marks: {df.describe().max()}")
#Find minimum marks.
print(f"Min Marks: {df.describe().min()}")

#Sort students by Python marks.
df= df.sort_values(["python_marks"])
print(df)
#Sort students by attendance.
df =  df.sort_values(["attendance"])
print(df)
#Filter students having Python marks greater than 80.
df = df[df["python_marks"]>80]
#Filter students having attendance greater than 75.
df =  df[df["attendance"]>75]
#Select only name, python_marks, and pandas_marks.
df= df[["name","python_marks","pandas_marks"]]
#Add a new column called total_marks.
df["total_marks"]=df["python_marks"]+df["pandas_marks"]
#Add another column called average_marks.
df["average_marks"] = df["total_marks"]/2
#Save the processed dataset into
df.to_csv("students_filer.csv", index=False)