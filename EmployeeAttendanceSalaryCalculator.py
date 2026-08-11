# ============================================
#    EMPLOYEE SALARY MANAGEMENT SYSTEM
# ============================================

# Welcome message
print("=" * 55)
print("    EMPLOYEE SALARY MANAGEMENT SYSTEM")
print("=" * 55)

# List to store all employee records
employees = []

# Get number of employees
try:
    n = int(input("\nEnter number of employees: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Input employee details
for i in range(n):
    print(f"\n--- Employee {i + 1} ---")

    name = input("Enter employee name: ").strip()

    # Validate salary
    try:
        salary_per_day = float(input("Enter salary per day: ₹"))
        if salary_per_day <= 0:
            print("Salary must be positive.")
            continue
    except ValueError:
        print("Invalid salary input.")
        continue

    # Validate days present
    try:
        days_present = int(input("Enter days present: "))
        if days_present < 0:
            print(" Days present cannot be negative.")
            continue
    except ValueError:
        print("Invalid days input.")
        continue

    # Validate late days
    try:
        late_days = int(input("Enter late days: "))
        if late_days < 0:
            print("Late days cannot be negative.")
            continue
    except ValueError:
        print("Invalid late days input.")
        continue

    # Calculate gross salary
    gross_salary = salary_per_day * days_present

    # Determine deduction based on late days
    if late_days > 10:
        deduction_rate = 20
    elif late_days >= 6:
        deduction_rate = 10
    elif late_days >= 3:
        deduction_rate = 5
    else:
        deduction_rate = 0

    deduction = gross_salary * deduction_rate / 100
    final_salary = gross_salary - deduction

    # Store employee record
    employees.append({
        "name": name,
        "gross": gross_salary,
        "deduction": deduction,
        "deduction_rate": deduction_rate,
        "final": final_salary,
        "late_days": late_days
    })

# Check if any employees were added
if not employees:
    print("\n No employee records to process.")
    exit()

# Display individual salary slips
print("\n")
print("=" * 70)
print("                   SALARY SLIPS")
print("=" * 70)
print(f"{'Name':<15}{'Gross':>12}{'Deduction':>15}{'Final Salary':>15}")
print("-" * 70)

for emp in employees:
    print(f"{emp['name']:<15}"
          f"{'₹' + format(emp['gross'], ','):>12}"
          f"{'₹' + format(round(emp['deduction'], 2), ','):>15}"
          f"{'₹' + format(round(emp['final'], 2), ','):>15}")

# Calculate company statistics
highest = max(employees, key=lambda e: e["final"])
lowest = min(employees, key=lambda e: e["final"])
total_payroll = sum(emp["final"] for emp in employees)

# Display company statistics
print("\n")
print("=" * 55)
print("          COMPANY PAYROLL STATISTICS")
print("=" * 55)
print(f" Highest Salary     : ₹{format(round(highest['final'], 2), ',')}")
print(f"   (Employee          : {highest['name']})")
print(f" Lowest Salary      : ₹{format(round(lowest['final'], 2), ',')}")
print(f"   (Employee          : {lowest['name']})")
print(f" Total Payroll      : ₹{format(round(total_payroll, 2), ',')}")
print(f" Top Earner         : {highest['name']} (₹{format(round(highest['final'], 2), ',')})")
print("=" * 55)
print(" Salary processing completed!")
print("=" * 55)
