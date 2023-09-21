class Student:
    def _init_(self, student_id, name, m1, m2, m3):
        self.student_id = student_id
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.gpa = self.calculateGPA()

    def calculateGPA(self):
        return (1/3) * self.m1 + (1/2) * self.m2 + (1/4) * self.m3

def display_all_students(students):
    print("Student Information:")
    for student in students:
        print(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa}")

def search_by_id(students, search_id):
    for student in students:
        if student.student_id == search_id:
            return student
    return None

def search_by_name(students, search_name):
    found_students = []
    for student in students:
        if student.name.lower() == search_name.lower():
            found_students.append(student)
    return found_students

def insert_student(students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    m1 = float(input("Enter marks for subject 1: "))
    m2 = float(input("Enter marks for subject 2: "))
    m3 = float(input("Enter marks for subject 3: "))
    
    student = Student(student_id, name, m1, m2, m3)
    students.append(student)
    print("Student details inserted successfully!")

def main():
    students = []

    while True:
        print("\nMenu:")
        print("1. Display All Students")
        print("2. Search by ID")
        print("3. Search by Name")
        print("4. Calculate GPA of a Student")
        print("5. Insert Student Detail")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_all_students(students)
        elif choice == "2":
            search_id = input("Enter student ID to search: ")
            student = search_by_id(students, search_id)
            if student:
                print(f"Student found - ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa}")
            else:
                print("Student not found.")
        elif choice == "3":
            search_name = input("Enter student name to search: ")
            found_students = search_by_name(students, search_name)
            if found_students:
                print("Found students with the given name:")
                for student in found_students:
                    print(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa}")
            else:
                print("No students found with the given name.")
        elif choice == "4":
            search_id = input("Enter student ID to calculate GPA: ")
            student = search_by_id(students, search_id)
            if student:
                print(f"GPA of Student {student.name}: {student.gpa}")
            else:
                print("Student not found.")
        elif choice == "5":
            insert_student(students)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()