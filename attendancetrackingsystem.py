
# SIMPLE ATTENDANCE CHECKING SYSTEM

# List to store student names
students = []

# Dictionary to store attendance {'date': {'student_name': 'status'}}
attendance = {}


# Function to display menu
def show_menu():
    print("\n" + "=" * 40)
    print("   ATTENDANCE CHECKING SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Take Attendance")
    print("4. View Attendance")
    print("5. Exit")
    print("=" * 40)


# Function to add students
def add_students():
    print("\n--- ADD STUDENTS ---")
    while True:
        name = input("Enter student name (or 'done' to stop): ").strip().title()
        if name.lower() == 'done':
            break
        if name:
            students.append(name)
            print(f"✅ {name} added!")
        else:
            print("❌ Name cannot be empty!")

    print(f"\nTotal students: {len(students)}")


# Function to view all students
def view_students():
    print("\n--- STUDENT LIST ---")
    if not students:
        print("No students added yet!")
    else:
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")


# Function to take attendance
def take_attendance():
    if not students:
        print("\n❌ No students! Please add students first.")
        return

    date = input("\nEnter date (YYYY-MM-DD): ").strip()

    if date in attendance:
        print(f"\n⚠️ Attendance for {date} already exists!")
        choice = input("Overwrite? (yes/no): ").lower()
        if choice != 'yes':
            print("Cancelled.")
            return

    attendance[date] = {}
    print(f"\n--- ATTENDANCE FOR {date} ---")
    print("Enter: p = Present, a = Absent\n")

    # Loop through each student
    for student in students:
        while True:
            status = input(f"{student} (p/a): ").lower()
            if status == 'p':
                attendance[date][student] = "Present"
                break
            elif status == 'a':
                attendance[date][student] = "Absent"
                break
            else:
                print("❌ Invalid! Enter 'p' or 'a'")

    # Show summary
    present = list(attendance[date].values()).count("Present")
    absent = len(students) - present
    print(f"\n✅ Attendance saved for {date}!")
    print(f"Present: {present} | Absent: {absent}")


# Function to view attendance
def view_attendance():
    if not attendance:
        print("\n❌ No attendance records yet!")
        return

    print("\n--- ATTENDANCE RECORDS ---")
    for date, records in attendance.items():
        print(f"\n📅 Date: {date}")
        print("-" * 30)

        present_count = 0
        for student, status in records.items():
            print(f"{student:<15} : {status}")
            if status == "Present":
                present_count += 1

        print("-" * 30)
        print(f"Present: {present_count}/{len(students)}")


# Main program loop
def main():
    print("🎓 WELCOME TO ATTENDANCE CHECKING SYSTEM 🎓")

    while True:
        show_menu()
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '1':
            add_students()
        elif choice == '2':
            view_students()
        elif choice == '3':
            take_attendance()
        elif choice == '4':
            view_attendance()
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Enter 1-5.")

        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()