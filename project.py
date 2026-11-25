# ============================================================
#   SGPA / CGPA / CLASS PERFORMANCE INDEX CALCULATOR
# ============================================================

# ---------- CPI SETTINGS (Bennett University) ----------
AVERAGE_WEIGHT = 0.7      # weight given to class average GPA
PASS_WEIGHT = 0.3         # weight given to pass percentage
DISTINCTION_GPA = 8.0     # GPA at or above this counts as distinction
PERCENTAGE_FACTOR = 9.5   # CGPA -> percentage conversion



# SGPA 
def get_sgpa():
    """Calculate SGPA for one semester from subject-wise data."""
    num_subjects = int(input("Enter number of subjects: "))

    total_credits = 0
    total_points = 0

    for i in range(1, num_subjects + 1):
        print("---- Subject", i, "----")

        subject = input("Enter subject name: ")
        credits = float(input("Enter credits: "))
        grade_point = float(input("Enter grade point (0-10): "))

        total_credits += credits
        total_points += credits * grade_point


    sgpa = total_points / total_credits
    return sgpa, total_credits


# OPTION 1: SGPA 
def sgpa_option():
    enrollment_number = input("Enter your enrollment number: ")
    semester = input("Enter semester number: ")

    sgpa, total_credits = get_sgpa()

    print("========== RESULT ==========")
    print("Enrollment:", enrollment_number)
    print("Semester:", semester)
    print("Total Credits:", total_credits)
    print("SGPA:", round(sgpa, 2))


# OPTION 2: CGPA
def cgpa_option():
    enrollment_number = input("Enter your enrollment number: ")
    num_semesters = int(input("Enter number of semesters completed: "))

    print("How do you want to enter semester data?")
    print("1. I already know my SGPA and credits")
    print("2. Calculate SGPA from subjects")

    method = input("Choose (1/2): ")
    while method not in ("1", "2"):
        method = input("Invalid. Choose 1 or 2: ")

    total_credits = 0
    total_points = 0

    for i in range(1, num_semesters + 1):
        print("######## Semester", i, "########")

        if method == "1":
            sgpa = float(input("Enter SGPA (0-10): "))
            credits = float(input("Enter total credits: "))
        else:
            sgpa, credits = get_sgpa()
            print("Semester", i, "SGPA:", round(sgpa, 2))

        total_credits += credits
        total_points += sgpa * credits


    cgpa = total_points / total_credits
    percentage = cgpa * PERCENTAGE_FACTOR

    required_cgpa = float(input("Enter required CGPA (0-10): "))

    print("========== RESULT ==========")
    print("Enrollment:", enrollment_number)
    print("Semesters:", num_semesters)
    print("Total Credits:", total_credits)
    print("CGPA:", round(cgpa, 2))
    print("Approx. Percentage:", round(percentage, 2), "%")
    print("Required CGPA:", required_cgpa)

    if cgpa >= required_cgpa:
        print("You are safe!")
        print("You are", round(cgpa - required_cgpa, 2),
              "above the required CGPA.")
    else:
        print("You are short of the required CGPA!")
        print("You need to improve by",
              round(required_cgpa - cgpa, 2), "points.")


# ---------- OPTION 3: CLASS PERFORMANCE INDEX ----------
def class_performance_option():
    class_name = input("Enter class / section name: ")
    num_students = int(input("Enter number of students: "))
    pass_gpa = float(input("Enter minimum passing GPA (e.g. 4): "))

    students = []

    for i in range(1, num_students + 1):
        name = input("Student " + str(i) + " name / enrollment: ")
        gpa = float(input("Enter SGPA / CGPA (0-10): "))
        students.append((name, gpa))

    gpas = [gpa for name, gpa in students]

    # Class statistics
    average = sum(gpas) / num_students
    highest = max(gpas)
    lowest = min(gpas)

    passed = len([g for g in gpas if g >= pass_gpa])
    pass_percentage = (passed / num_students) * 100

    distinction = len([g for g in gpas if g >= DISTINCTION_GPA])
    distinction_percentage = (distinction / num_students) * 100

    # Class Performance Index (out of 100)
    cpi = (AVERAGE_WEIGHT * (average * 10)) + (PASS_WEIGHT * pass_percentage)

    if cpi >= 85:
        rating = "Outstanding"
    elif cpi >= 75:
        rating = "Very Good"
    elif cpi >= 60:
        rating = "Good"
    elif cpi >= 50:
        rating = "Average"
    else:
        rating = "Needs Improvement"

    print("========== CLASS REPORT ==========")
    print("Class:", class_name)
    print("Total Students:", num_students)
    print("Class Average GPA:", round(average, 2))
    print("Highest GPA:", highest)
    print("Lowest GPA:", lowest)
    print("Passed:", passed, "(", round(pass_percentage, 1), "%)")
    print("Distinction:", distinction,
          "(", round(distinction_percentage, 1), "%)")

    print("CLASS PERFORMANCE INDEX:", round(cpi, 2), "/ 100")
    print("Rating:", rating)

    # Rank list
    ranked = sorted(students, key=lambda s: s[1], reverse=True)

    print("---------- RANK LIST ----------")
    for rank, (name, gpa) in enumerate(ranked, start=1):
        status = "Pass" if gpa >= pass_gpa else "Fail"
        print(rank, "-", name, "-", gpa, "-", status)


# MAIN MENU
def main():
    print()
    print("  SGPA / CGPA / CLASS INDEX")
    print()
    while True:
        print("1. Calculate SGPA")
        print("2. Calculate CGPA")
        print("3. Class Performance Index")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            sgpa_option()
        elif choice == "2":
            cgpa_option()
        elif choice == "3":
            class_performance_option()
        elif choice == "4":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


main()