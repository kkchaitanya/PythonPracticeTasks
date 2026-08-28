import random

import pandas as pd
class Student:
    def __init__(self, student_id, name, email, phone, course, city):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.phone = phone
        self.course = course
        self.city = city

    def display(self):
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Phone      : {self.phone}")
        print(f"Course     : {self.course}")
        print(f"City       : {self.city}")

class StudentRegistrationSystem:
    def __init__(self,student:Student):
        self.student = student
        self.new_student = pd.DataFrame({
                    "student_id": [self.student.student_id],
                    "name": [self.student.name],
                    "email": [self.student.email],
                    "phone": [self.student.phone],
                    "course": [self.student.course],
                    "city": [self.student.city]
                })
    def creat_file(self):
         self.new_student.to_csv(
                     "students.txt",index=False,
                 )
    def append_student_info_to_file(self):
        self.new_student.to_csv(
            "students.txt",
            mode="a",
            index=False,
            header=False
        )

    
def load_studnets_info():
           df= pd.read_csv("students.txt")
           return  df

def backup_data(students_bakup):
        students_bakup.to_csv(
                        "students_backup.txt",
                    )

student1 = Student(
    101,
    "Krishna",
    "krishna@gmail.com",
    "9876543210",
    "Python",
    "Hyderabad"
)

# student1.display()
strs= StudentRegistrationSystem(student1)
strs.creat_file()
student2 = Student(
    102,
    "Hari",
    "hari@gmail.com",
    "9876543210",
    "Java",
    "Hyderabad"
)
# student2.display()
strs= StudentRegistrationSystem(student2)
strs.append_student_info_to_file()

for i in range(2, 25):
    student = Student(
                102+int(i),
                random.choice([f"Hari{str(i)}",f"Giri{str(i)}",f"Ram{str(i)}"]),
                random.choice([f"hari{str(i)}@gmail.com",f"giri{str(i)}@gmail.com",f"ram{str(i)}@gmail.com"]),
                random.randint(6000000000, 9999999999),
                random.choice(["Java","Python",'DOTNET']),
                random.choice(["Hyderabad","Delhi","Banglore"])
            )
    strs= StudentRegistrationSystem(student)
    strs.append_student_info_to_file()

## Read complete records.
lsi = load_studnets_info()
## Read individual lines.
for line in lsi.iterrows():
     print(line)
## Count number of records.
print(f"number of records: {len(lsi)}")
## Copy data into another backup file.
backup_data(lsi)
## Create another file containing only names and courses.
name_cource= lsi[["name","course"]]
name_cource.to_csv("student_name_course.txt",index=False,)