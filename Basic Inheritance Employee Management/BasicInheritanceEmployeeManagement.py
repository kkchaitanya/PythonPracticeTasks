# ==========================================
# INHERITANCE IN PYTHON
# Employee -> Developer, Manager, HR
# ==========================================


# ------------------------------------------
# Parent Class
# ------------------------------------------

class Employee:

    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    # Parent class method
    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

    # Parent class method
    def calculate_salary(self):
        print("Monthly Salary:", self.salary)


# ------------------------------------------
# Child Class 1: Developer
# ------------------------------------------

class Developer(Employee):

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        programming_language
    ):
        # Calling parent class constructor
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        self.programming_language = programming_language

    def display_developer_details(self):
        print("Programming Language:", self.programming_language)


# ------------------------------------------
# Child Class 2: Manager
# ------------------------------------------

class Manager(Employee):

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        team_size
    ):
        # Calling parent class constructor
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        self.team_size = team_size

    def display_manager_details(self):
        print("Team Size:", self.team_size)


# ------------------------------------------
# Child Class 3: HR
# ------------------------------------------

class HR(Employee):

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        region
    ):
        # Calling parent class constructor
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        self.region = region

    def display_hr_details(self):
        print("Region:", self.region)


# ==========================================
# Creating Developer Objects
# ==========================================

developer1 = Developer(
    101,
    "Rahul",
    60000,
    "Development",
    "Python"
)

developer2 = Developer(
    102,
    "Priya",
    65000,
    "Development",
    "Java"
)


# ==========================================
# Creating Manager Objects
# ==========================================

manager1 = Manager(
    201,
    "Arjun",
    90000,
    "Management",
    10
)

manager2 = Manager(
    202,
    "Sneha",
    95000,
    "Management",
    15
)


# ==========================================
# Creating HR Objects
# ==========================================

hr1 = HR(
    301,
    "Vikram",
    55000,
    "Human Resources",
    "South India"
)

hr2 = HR(
    302,
    "Ananya",
    58000,
    "Human Resources",
    "North India"
)


# ==========================================
# Demonstrating Developer Objects
# ==========================================

print("\n================================")
print("DEVELOPER 1")
print("================================")

# Inherited method from Employee
developer1.display_details()

# Inherited method from Employee
developer1.calculate_salary()

# Child-specific attribute
print("Programming Language:", developer1.programming_language)

# Child-specific method
developer1.display_developer_details()


print("\n================================")
print("DEVELOPER 2")
print("================================")

developer2.display_details()
developer2.calculate_salary()
print("Programming Language:", developer2.programming_language)
developer2.display_developer_details()


# ==========================================
# Demonstrating Manager Objects
# ==========================================

print("\n================================")
print("MANAGER 1")
print("================================")

manager1.display_details()
manager1.calculate_salary()

# Child-specific attribute
print("Team Size:", manager1.team_size)

# Child-specific method
manager1.display_manager_details()


print("\n================================")
print("MANAGER 2")
print("================================")

manager2.display_details()
manager2.calculate_salary()
print("Team Size:", manager2.team_size)
manager2.display_manager_details()


# ==========================================
# Demonstrating HR Objects
# ==========================================

print("\n================================")
print("HR 1")
print("================================")

hr1.display_details()
hr1.calculate_salary()

# Child-specific attribute
print("Region:", hr1.region)

# Child-specific method
hr1.display_hr_details()


print("\n================================")
print("HR 2")
print("================================")

hr2.display_details()
hr2.calculate_salary()
print("Region:", hr2.region)
hr2.display_hr_details()
