# Parent Class
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def display_info(self):
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


# Course Class
class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title

    def __str__(self):
        return f"{self.course_id} - {self.title}"


# Child Class: Student
class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.enrolled_courses = {}
        # Dictionary: {course: progress}

    def enroll_course(self, course):
        self.enrolled_courses[course] = 0
        print(f"{self.name} enrolled in {course.title}")

    def update_progress(self, course, progress):
        if course in self.enrolled_courses:
            self.enrolled_courses[course] = progress

    def view_courses(self):
        print(f"\nCourses enrolled by {self.name}:")
        for course in self.enrolled_courses:
            print(course)

    def check_progress(self):
        print(f"\nProgress Report for {self.name}:")
        for course, progress in self.enrolled_courses.items():
            print(f"{course.title}: {progress}% completed")


# Child Class: Instructor
class Instructor(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.teaching_courses = []

    def create_course(self, course):
        self.teaching_courses.append(course)
        print(f"{self.name} created course: {course.title}")

    def display_courses(self):
        print(f"\nCourses taught by {self.name}:")
        for course in self.teaching_courses:
            print(course)


# ---------------------------
# Creating Instructors
# ---------------------------
instructor1 = Instructor(201, "Anitha", "anitha@example.com")
instructor2 = Instructor(202, "Swaminathan", "swami@example.com")

# Creating Courses
course1 = Course("C101", "Python Programming")
course2 = Course("C102", "Data Structures")
course3 = Course("C103", "Web Development")

# Instructors creating courses
instructor1.create_course(course1)
instructor1.create_course(course2)
instructor2.create_course(course3)

# Display instructor courses
instructor1.display_courses()
instructor2.display_courses()


# ---------------------------
# Creating Students
# ---------------------------
student1 = Student(101, "Krishna", "krishna@example.com")
student2 = Student(102, "Rahul", "rahul@example.com")

# Students enrolling in courses
student1.enroll_course(course1)
student1.enroll_course(course3)

student2.enroll_course(course2)
student2.enroll_course(course3)

# Updating progress
student1.update_progress(course1, 75)
student1.update_progress(course3, 50)

student2.update_progress(course2, 40)
student2.update_progress(course3, 90)

# Viewing enrolled courses
student1.view_courses()
student2.view_courses()

# Checking course progress
student1.check_progress()
student2.check_progress()


# ---------------------------
# Demonstrating Inheritance
# ---------------------------
print("\n--- Inheritance Demonstration ---")
student1.display_info()       # Inherited from User
print()
instructor1.display_info()    # Inherited from User