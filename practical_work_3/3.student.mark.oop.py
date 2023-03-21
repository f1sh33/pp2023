import numpy as np

class Student:
    def __init__(self, name, student_id, date_of_birth):
        self.name = name
        self.student_id = student_id
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"{self.name} - {self.student_id}"

class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = {'name': student.name, 'marks': {}}

    def input_marks(self, student_id):
        mark = input(f"Enter mark for student {self.students[student_id]['name']} in {self.name}: ")
        self.students[student_id]['marks'][self.course_id] = mark

    def get_credit(self):
        return int(self.credit)

    def return_mark(self, student_id):
        mark = self.students[student_id]['marks'][self.course_id];
        return int(mark)

    def list_students(self):
        for student_info in self.students.values():
            print(student_info['name'])

    def list_marks(self):
        for student_id, student_info in self.students.items():
            if self.course_id in student_info['marks']:
                mark = student_info['marks'][self.course_id]
                print(f"{student_info['name']} ({student_id}): {mark}")

class MarkManagement:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_students(self, num_students):
        for i in range(num_students):
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            dob = input("Enter student date of birth (YYYY-MM-DD): ")
            self.students[student_id] = Student(name, student_id, dob)

    def input_courses(self, num_courses):
        for i in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credit = int(input("Enter number of credits for this course: "))
            self.courses[course_id] = Course(course_id, name, credit)

    def input_students_to_courses(self):
        for course in self.courses.values():
            for student in self.students.values():
                course.add_student(student)

    def input_marks(self):
        for course in self.courses.values():
            for student_id in course.students.keys():
                course.input_marks(student_id)

    """ def calculate_gpa(self):
        for student_id in self.students.keys():
            credit_array = [for credit in self.courses.val] """

    def list_courses(self):
        print("Courses:")
        for course in self.courses.values():
            print(course.name)

    def list_students(self):
        print("Students:")
        for student in self.students.values():
            print(student)

    def list_marks(self):
        print("Marks:")
        for course in self.courses.values():
            print(course.name)
            course.list_marks()
    
    def list_gpa(self):
        credit_array = []
        for course in self.courses.values():
            credit_array.append(course.get_credit())
        for student_id, student in self.students.items():
            marks = []
            for course in self.courses.values():
                marks.append(course.return_mark(student_id))
            weighted_sum = np.array(marks) * np.array(credit_array)
            total_weighted_sum = np.sum(weighted_sum)
            total_credit = np.sum(credit_array)
            gpa = total_weighted_sum/total_credit
            print(f'GPA of Student {student_id} is {gpa}')

mm = MarkManagement()

num_students = int(input("Enter number of students: "))
mm.input_students(num_students)

num_courses = int(input("Enter number of courses: "))
mm.input_courses(num_courses)

mm.input_students_to_courses()

mm.input_marks()

mm.list_courses()
mm.list_students()
mm.list_marks()
mm.list_gpa()