manage.clear_data([student_file, course_file, mark_file])

student_number = input.student_number()
for i in range (0, student_number):
    student_info = input.student()
    students.create_student(student_file, student_info)

course_number = input.course_number()
for i in range (0, course_number):
    course_info = input.course()
    courses.create_course(course_file, course_info)
