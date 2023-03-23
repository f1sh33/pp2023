import os

import input
import output
from domains import students
from domains import courses
from domains import manage

student_file = os.path.abspath("./practical_work_4/pw4/data/students.csv")
course_file = os.path.abspath("./practical_work_4/pw4/data/courses.csv")
mark_file = os.path.abspath("./practical_work_4/pw4/data/mark.csv")

manage.clear_data([student_file, course_file, mark_file])

student_number = input.student_number()
for i in range (0, student_number):
    student_info = input.student()
    students.create_student(student_file, student_info)

course_number = input.course_number()
for i in range (0, course_number):
    course_info = input.course()
    courses.create_course(course_file, course_info)

manage.input_mark(student_file, course_file, mark_file)
manage.list_courses(course_file)
manage.list_student(student_file)
manage.calculate_gpa(student_file, course_file, mark_file)
