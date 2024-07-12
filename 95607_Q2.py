# Define the school class management system

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students in the class.")
        else:
            print("List of students:")
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average_grade(self, student_name):
        for student in self.students:
            if student.name == student_name:
                grades = student.grades.values()
                if grades:
                    average_grade = sum(grades) / len(grades)
                    print(f"Average grade for {student_name}: {average_grade}")
                else:
                    print(f"No grades found for {student_name}.")
                return
        print(f"Student {student_name} not found.")

    def get_class_average_subject(self, subject):
        total_grades = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total_grades += student.grades[subject]
                count += 1
        if count > 0:
            class_average = total_grades / count
            print(f"Class average for {subject}: {class_average}")
        else:
            print(f"No students have grades for {subject}.")

# Main program
classroom = Classroom()

# Adding students
student1 = Student("Alice")
student1.grades = {"Math": 85, "History": 90}
student2 = Student("Bob")
student2.grades = {"Math": 92, "History": 88}
classroom.add_student(student1)
classroom.add_student(student2)

# Demonstrating functionalities
classroom.display_students()
classroom.get_student_average_grade("Alice")
classroom.get_class_average_subject("Math")
