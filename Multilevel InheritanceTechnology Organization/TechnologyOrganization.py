# Multilevel Inheritance Demonstration
# Person -> Employee -> Developer


# --------------------------------------------------
# Level 1: Person
# --------------------------------------------------

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def show_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

    def introduce(self):
        print("Hello, my name is", self.name)


# --------------------------------------------------
# Level 2: Employee
# Inherits from Person
# --------------------------------------------------

class Employee(Person):
    def __init__(self, name, age, city, employee_id, salary, company):
        super().__init__(name, age, city)

        self.employee_id = employee_id
        self.salary = salary
        self.company = company

    def show_employee_details(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Company:", self.company)

    def work(self):
        print(self.name, "is working at", self.company)


# --------------------------------------------------
# Level 3: Developer
# Inherits from Employee
# --------------------------------------------------

class Developer(Employee):
    def __init__(
        self,
        name,
        age,
        city,
        employee_id,
        salary,
        company,
        language,
        framework,
        experience
    ):
        super().__init__(
            name,
            age,
            city,
            employee_id,
            salary,
            company
        )

        self.language = language
        self.framework = framework
        self.experience = experience

    def show_developer_details(self):
        print("Programming Language:", self.language)
        print("Framework:", self.framework)
        print("Experience:", self.experience, "years")

    def code(self):
        print(
            self.name,
            "is coding in",
            self.language,
            "using",
            self.framework
        )


# --------------------------------------------------
# Creating 5 Developer objects
# --------------------------------------------------

developer1 = Developer(
    "Rahul", 25, "Hyderabad",
    "E101", 60000, "TechCorp",
    "Python", "Django", 3
)

developer2 = Developer(
    "Priya", 28, "Bangalore",
    "E102", 75000, "Infosys",
    "Java", "Spring", 5
)

developer3 = Developer(
    "Arjun", 24, "Chennai",
    "E103", 55000, "TCS",
    "JavaScript", "React", 2
)

developer4 = Developer(
    "Sneha", 30, "Mumbai",
    "E104", 90000, "Wipro",
    "Python", "Flask", 7
)

developer5 = Developer(
    "Vikram", 27, "Pune",
    "E105", 70000, "Accenture",
    "C#", ".NET", 4
)


# --------------------------------------------------
# Demonstrating the first Developer object
# --------------------------------------------------

print("========================================")
print("DEVELOPER 1 DETAILS")
print("========================================")

# Properties from Person
print("\n--- Person Properties ---")
print("Name:", developer1.name)
print("Age:", developer1.age)
print("City:", developer1.city)

# Properties from Employee
print("\n--- Employee Properties ---")
print("Employee ID:", developer1.employee_id)
print("Salary:", developer1.salary)
print("Company:", developer1.company)

# Properties from Developer
print("\n--- Developer Properties ---")
print("Language:", developer1.language)
print("Framework:", developer1.framework)
print("Experience:", developer1.experience, "years")


# --------------------------------------------------
# Accessing methods from all three levels
# --------------------------------------------------

print("\n--- Person Methods ---")
developer1.introduce()
developer1.show_person_details()

print("\n--- Employee Methods ---")
developer1.work()
developer1.show_employee_details()

print("\n--- Developer Methods ---")
developer1.code()
developer1.show_developer_details()


# --------------------------------------------------
# Displaying all 5 Developer objects
# --------------------------------------------------

developers = [
    developer1,
    developer2,
    developer3,
    developer4,
    developer5
]

print("\n\n========================================")
print("ALL DEVELOPERS")
print("========================================")

for developer in developers:
    print("\n------------------------------")
    print("Name:", developer.name)
    print("Age:", developer.age)
    print("City:", developer.city)
    print("Employee ID:", developer.employee_id)
    print("Salary:", developer.salary)
    print("Company:", developer.company)
    print("Language:", developer.language)
    print("Framework:", developer.framework)
    print("Experience:", developer.experience, "years")

    # Method inherited from Person
    developer.introduce()

    # Method inherited from Employee
    developer.work()

    # Method defined in Developer
    developer.code()

