

# University class
class University:
    def init(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)
        print(f"Department {department} added.")

    def remove_department(self, department):
        try:
            self.departments.remove(department)
            print(f"Department {department} removed.")
        except ValueError:
            print(f"Cannot remove {department}, it doesn't exist.")

    def get_departments(self):
        print("Departments:", self.departments)

    def search_department(self, department):
        print(f"{department} found.") if department in self.departments else print(f"{department} not found.")

    def edit_department(self, old_department, new_department):
        try:
            index = self.departments.index(old_department)
            self.departments[index] = new_department
            print(f"Department {old_department} changed to {new_department}.")
        except ValueError:
            print(f"Department {old_department} not found.")

# Base class Person
class Person:
    def init(self, name, age, contact, role):
        self.name = name
        self.age = age
        self.contact = contact
        self.role = role

# Teacher class inheriting from Person
class Teacher(Person):
    def init(self, name, age, contact, departments, file_name):
        super().init(name, age, contact, role="Teacher")
        self.departments = departments
        self.file_name = file_name

    def set_departments_teacher(self, departments):
        self.departments = departments

    def get_departments_teacher(self):
        print("Teacher's departments:", self.departments)

    def get_particular_departments(self, department_name):
        print(f"{department_name} is one of the departments.") if department_name in self.departments else print(f"{department_name} is not assigned.")

    def update_department_courses(self, department, course):
        print(f"Course {course} updated in department {department}.")

    def remove_department_courses(self, department, course):
        print(f"Course {course} removed from department {department}.")


# Student class inheriting from Person
class Student(Person):
    def init(self, name, age, contact, department, semester, courses, file_name):
        super().init(name, age, contact, role="Student")
        self.department = department
        self.semester = semester
        self.courses = courses
        self.file_name = file_name

    def set_courses(self, courses):
        self.courses = courses

    def update_course(self, old_course, new_course):
        try:
            index = self.courses.index(old_course)
            self.courses[index] = new_course
            print(f"Course {old_course} updated to {new_course}.")
        except ValueError:
            print(f"Course {old_course} not found.")

    def update_instructor(self, instructor):
        print(f"Instructor {instructor} updated.")

    def clear_courses(self):
        self.courses.clear()
        print("All courses cleared.")

    def remove_course(self, course):
        try:
            self.courses.remove(course)
            print(f"Course {course} removed.")
        except ValueError:
            print(f"Course {course} not found.")


# Example Usage
university = University("National textile university")
university.add_department("Computer Science")
university.add_department("Mathematics")
university.get_departments()
university.remove_department("Mathematics")
university.get_departments()

teacher = Teacher(name="Ali", age=30, contact="12345", departments=["Computer Science"], file_name="teacher_info.txt")
teacher.get_departments_teacher()
teacher.update_department_courses("Computer Science", "AI")

student = Student(name="Aimna", age=20, contact="67890", department="Computer Science", semester="4th", courses=["AI", "ML"], file_name="student_info.txt")
student.update_course("AI", "Deep Learning")
student.remove_course("ML")