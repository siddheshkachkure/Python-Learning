
class hpc_2023_Lab_Exam:
    def verify_cdac_student(self):
        student_name = input("Enter student name: ")
        if student_name.startswith("cdac") and student_name.endswith("pune"):
            with open("student_data.txt", "a") as f:
                f.write(student_name + "\n")
            print("Student added successfully!")
        else:
            print("Invalid student entry")

    def read_student_details_from_file(self):
        admitted_student = []
        with open("student_data.txt", "r") as f:
            for line in f:
                admitted_student.append(line.strip())
        return admitted_student


class hpc_2023(hpc_2023_Lab_Exam):
    def display_student_name_with_status(self):
        admitted_student = self.read_student_details_from_file()
        active_students = [name + "_active" for name in admitted_student]
        print("Active students:")
        for student in active_students:
            print(student)

hpc = hpc_2023()
while True:
    print("\nChoose an option:")
    print("1. Add student")
    print("2. Display active students")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        hpc.verify_cdac_student()
    elif choice == "2":
        hpc.display_student_name_with_status()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
