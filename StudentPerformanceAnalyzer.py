# ============================================
#    STUDENT MARKS MANAGEMENT SYSTEM
# ============================================

# Welcome message
print("=" * 60)
print("   🎓 STUDENT MARKS MANAGEMENT SYSTEM 🎓")
print("=" * 60)

# List to store all student records
students = []

# Get number of students
try:
    n = int(input("\nEnter the number of students: "))
    if n <= 0:
        print("❌ Number of students must be greater than 0.")
        exit()
except ValueError:
    print("❌ Please enter a valid number.")
    exit()

# Input student details
for i in range(n):
    print(f"\n{'─' * 50}")
    print(f"  📘 Student {i + 1}")
    print(f"{'─' * 50}")

    name = input("Enter student name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        continue

    # Input marks for 5 subjects
    subjects = ["English", "Maths", "Science", "Social", "Computer"]
    marks = {}

    valid = True
    for subject in subjects:
        try:
            mark = float(input(f"  Marks in {subject} (out of 100): "))
            if mark < 0 or mark > 100:
                print(f"❌ Marks for {subject} must be between 0 and 100.")
                valid = False
                break
            marks[subject] = mark
        except ValueError:
            print(f"❌ Invalid marks for {subject}.")
            valid = False
            break

    if not valid:
        print("⚠️  Skipping this student due to invalid input.")
        continue

    # Calculate total and percentage
    total = sum(marks.values())
    percentage = total / len(subjects)

    # Determine grade
    if percentage >= 90:
        grade = "A"
        remark = "Outstanding 🌟"
    elif percentage >= 75:
        grade = "B"
        remark = "Very Good 👍"
    elif percentage >= 60:
        grade = "C"
        remark = "Good ✅"
    elif percentage >= 40:
        grade = "D"
        remark = "Needs Improvement 📚"
    else:
        grade = "F"
        remark = "Failed ❌"

    # Pass/Fail status (fail if any subject < 40)
    status = "Pass" if all(m >= 40 for m in marks.values()) else "Fail"

    # Store student record
    students.append({
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "remark": remark,
        "status": status
    })

# Check if any students were added
if not students:
    print("\n❌ No valid student records to display.")
    exit()

# ---------- CLASS STATISTICS ----------
highest = max(students, key=lambda s: s["percentage"])
lowest = min(students, key=lambda s: s["percentage"])
avg_percentage = sum(s["percentage"] for s in students) / len(students)
failed_count = sum(1 for s in students if s["status"] == "Fail")

# ---------- DISPLAY INDIVIDUAL REPORT ----------
print("\n")
print("=" * 80)
print("                  📋 INDIVIDUAL STUDENT REPORTS")
print("=" * 80)

for idx, s in enumerate(students, start=1):
    print(f"\n📘 Student {idx} : {s['name']}")
    print("─" * 60)
    print(f"{'Subject':<15}{'Marks':>15}")
    print("─" * 60)
    for subject, mark in s["marks"].items():
        print(f"{subject:<15}{mark:>15.1f}")
    print("─" * 60)
    print(f"  Total Marks      : {s['total']:.1f} / 500")
    print(f"  Percentage       : {s['percentage']:.2f}%")
    print(f"  Grade            : {s['grade']}  ({s['remark']})")
    print(f"  Result           : {s['status']}")

# ---------- DISPLAY SUMMARY TABLE ----------
print("\n")
print("=" * 80)
print("                   📊 CLASS SUMMARY REPORT")
print("=" * 80)
print(f"{'Name':<15}{'Total':>10}{'%':>10}{'Grade':>10}{'Status':>10}")
print("─" * 80)
for s in students:
    print(f"{s['name']:<15}{s['total']:>10.1f}"
          f"{s['percentage']:>10.2f}{s['grade']:>10}{s['status']:>10}")

# ---------- CLASS STATISTICS ----------
print("\n")
print("=" * 80)
print("                🏆 CLASS STATISTICS")
print("=" * 80)
print(f"  🥇 Highest Scorer         : {highest['name']} ({highest['percentage']:.2f}%) - Grade {highest['grade']}")
print(f"  🥉 Lowest Scorer          : {lowest['name']} ({lowest['percentage']:.2f}%) - Grade {lowest['grade']}")
print(f"  📊 Average Class %        : {avg_percentage:.2f}%")
print(f"  ❌ Students Who Failed     : {failed_count} out of {len(students)}")
print(f"  ✅ Students Who Passed     : {len(students) - failed_count} out of {len(students)}")
print("=" * 80)
print("         ✅ Report generated successfully!")
print("=" * 80)
